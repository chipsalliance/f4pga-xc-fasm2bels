#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2021-2022 F4PGA Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

from fpga_interchange.interchange_capnp import Interchange, write_capnp_file
from fpga_interchange.logical_netlist import LogicalNetlist, Library, Cell, \
        Direction, CellInstance
from fpga_interchange.physical_netlist import Placement, PhysicalPip, \
        PhysicalBelPin, PhysicalSitePin, PhysicalSitePip, PhysicalNetlist, \
        PhysicalNetType
from ..models.utils import make_bus, flatten_wires, unescape_verilog_name


class PhysicalBelPinWithDirection(PhysicalBelPin):
    def __init__(self, site, bel, pin, direction):
        super().__init__(site, bel, pin)

        self.site_source = False

        if direction == 'inout':
            self.direction = Direction.Inout
        elif direction == 'input':
            self.direction = Direction.Input
        elif direction == 'output':
            self.direction = Direction.Output
        else:
            assert direction == 'site_source'
            self.direction = Direction.Output
            self.site_source = True

    def nodes(self, cursor, site_type_pins):
        return []

    def is_root(self):
        return self.direction in [Direction.Output, Direction.Inout
                                  ] and not self.site_source


class PhysicalPipForStitching(PhysicalPip):
    def nodes(self, cursor, site_type_pins):
        cursor.execute("""SELECT pkey FROM phy_tile WHERE name = ?;""",
                       (self.tile, ))
        (phy_tile_pkey, ) = cursor.fetchone()

        cursor.execute(
            """
SELECT node_pkey FROM wire WHERE
    phy_tile_pkey = ?
AND
    wire_in_tile_pkey IN (SELECT pkey FROM wire_in_tile WHERE name = ?);""",
            (phy_tile_pkey, self.wire0))
        (node0_pkey, ) = cursor.fetchone()

        cursor.execute(
            """
SELECT node_pkey FROM wire WHERE
    phy_tile_pkey = ?
AND
    wire_in_tile_pkey IN (SELECT pkey FROM wire_in_tile WHERE name = ?);""",
            (phy_tile_pkey, self.wire1))
        (node1_pkey, ) = cursor.fetchone()

        return [node0_pkey, node1_pkey]

    def is_root(self):
        return False


class PhysicalSitePipForStitching(PhysicalSitePip):
    def nodes(self, cursor, site_type_pins):
        return []

    def is_root(self):
        return False


class PhysicalSitePinForStitching(PhysicalSitePin):
    def nodes(self, cursor, site_type_pins):
        cursor.execute(
            """
WITH a_site_instance(site_pkey, phy_tile_pkey) AS (
    SELECT site_pkey, phy_tile_pkey
    FROM site_instance
    WHERE name = ?
)
SELECT node_pkey FROM wire WHERE
    phy_tile_pkey = (SELECT phy_tile_pkey FROM a_site_instance)
AND
    wire_in_tile_pkey = (
        SELECT pkey FROM wire_in_tile WHERE
            site_pkey = (SELECT site_pkey FROM a_site_instance)
        AND
            site_pin_pkey IN (SELECT pkey FROM site_pin WHERE name = ?)
    );
        """, (self.site, site_type_pins[self.site, self.pin]))

        results = cursor.fetchall()
        assert len(results) == 1, (results, self.site, self.pin,
                                   site_type_pins[self.site, self.pin])
        return [results[0][0]]

    def is_root(self):
        return False


def convert_tuple_to_object(site, tup):
    """ Convert physical netlist tuple to object.

    Physical netlist tuples are light weight ways to represent the physical
    net tree.

    site (Site) - Site object that tuple belongs too.
    tup (tuple) - Tuple that is either a site pin, bel pin, or site pip.

    Returns - PhysicalSitePin, PhysicalBelPin, or PhysicalSitePip based on
              tuple.

    >>> Site = namedtuple('Site', 'name')
    >>> site = Site(name='TEST_SITE')

    >>> site_pin = convert_tuple_to_object(site, ('site_pin', 'TEST_PIN'))
    >>> assert isinstance(site_pin, PhysicalSitePin)
    >>> site_pin.site
    'TEST_SITE'
    >>> site_pin.pin
    'TEST_PIN'
    >>> site_pin.branches
    []

    >>> bel_pin = convert_tuple_to_object(site, ('bel_pin', 'ABEL', 'APIN', 'input'))
    >>> assert isinstance(bel_pin, PhysicalBelPin)
    >>> bel_pin.site
    'TEST_SITE'
    >>> bel_pin.bel
    'ABEL'
    >>> bel_pin.pin
    'APIN'
    >>> bel_pin.direction
    Direction.Input

    >>> site_pip = convert_tuple_to_object(site, ('site_pip', 'BBEL', 'BPIN'))
    >>> assert isinstance(site_pip, PhysicalSitePip)
    >>> site_pip.site
    'TEST_SITE'
    >>> site_pip.bel
    'BBEL'
    >>> site_pip.pin
    'BPIN'

    """
    if tup[0] == 'site_pin':
        _, pin = tup
        return PhysicalSitePinForStitching(site.name, pin)
    elif tup[0] == 'bel_pin':
        assert len(tup) == 4, tup
        _, bel, pin, direction = tup
        return PhysicalBelPinWithDirection(site.name, bel, pin, direction)
    elif tup[0] == 'site_pip':
        _, bel, pin = tup
        return PhysicalSitePipForStitching(site.name, bel, pin)
    else:
        assert False, tup


def add_site_routing_children(site, parent_obj, parent_key, site_routing,
                              inverted_root):
    """ Convert site_routing map into Physical* python objects.

    site (Site) - Site object that contains site routing.
    parent_obj (Physical* python object) - Parent Physical* object to add new
                                         branches too.
    parent_key (tuple) - Site routing tuple for current parent_obj.
    site_routing (dict) - Map of parent site routing tuple to a set of
                          child site routing tuples.
    inverted_root (list) - List of physical net sources for the inverted
                           signal (e.g. a constant 1 net inverts to the
                           constant 0 net)

    """
    if parent_key in site_routing:
        for child in site_routing[parent_key]:
            if child[0] == 'inverter':
                if inverted_root is not None:
                    for child2 in site_routing[child]:
                        obj = convert_tuple_to_object(site, child2)
                        inverted_root.append(obj)

                        # Continue to descend, but no more inverted root.
                        # There should be no double site inverters (hopefully?)
                        add_site_routing_children(
                            site,
                            obj,
                            child2,
                            site_routing,
                            inverted_root=None)
                else:
                    add_site_routing_children(site, parent_obj, child,
                                              site_routing, inverted_root)
            else:
                obj = convert_tuple_to_object(site, child)
                parent_obj.branches.append(obj)

                add_site_routing_children(site, obj, child, site_routing,
                                          inverted_root)


def create_site_routing(site, net_roots, site_routing, constant_nets):
    """ Convert site_routing into map of nets to site local sources.

    site (Site) - Site object that contains site routing.
    net_roots (dict) - Map of root site routing tuples to the net name for
                       this root.
    site_routing (dict) - Map of parent site routing tuple to a set of
                          child site routing tuples.
    constant_nets (dict) - Map of 0/1 to their net name.

    Returns dict of nets to Physical* objects that represent the site local
    sources for that net.

    """
    nets = {}

    # Create a map of constant net names to their inverse.
    inverted_roots = {}

    for value, net_name in constant_nets.items():
        nets[net_name] = []
        inverted_roots[constant_nets[value ^ 1]] = nets[net_name]

    for root, net_name in net_roots.items():
        if net_name not in nets:
            nets[net_name] = []

        root_obj = convert_tuple_to_object(site, root)
        add_site_routing_children(site, root_obj, root, site_routing,
                                  inverted_roots.get(net_name, None))

        nets[net_name].append(root_obj)

    return nets


class NodeCache():
    """ Cache of route segment to node_pkey and node_pkey to route segments. """

    def __init__(self):
        self.id_to_obj = {}
        self.id_to_nodes = {}
        self.node_to_ids = {}

    def add_route_branch(self, obj, cursor, site_type_pins):
        """ Add route branch to cache.

        obj : PhysicalBelPin/PhysicalSitePin/PhysicalSitePip/PhysicalPip
            Add route segment to node cache.

        cursor : sqlite3.Cursor
            Cursor to connection database.

        site_type_pins
            Map of used site pin to the site pin default name.

            The interchange uses the site pin name for the particular type in
            use, e.g. RAMB36E1.  The connection database has the site pin
            names for the default site type (e.g. RAMBFIFO36E1).
            site_type_pins maps the site specific type back to the default
            type found in the connection database.

            FIXME: If the connection database had the site pins for each
            alternative site type, this map would no longer be required.
        """
        obj_id = id(obj)
        assert obj_id not in self.id_to_obj

        self.id_to_obj[obj_id] = obj
        self.id_to_nodes[obj_id] = set(obj.nodes(cursor, site_type_pins))
        for node in self.id_to_nodes[obj_id]:
            if node not in self.node_to_ids:
                self.node_to_ids[node] = set()

            self.node_to_ids[node].add(obj_id)

        for child_branch in obj.branches:
            self.add_route_branch(child_branch, cursor, site_type_pins)

    def check_tree(self, obj, parent=None):
        """ Check that the routing tree at and below obj is valid.

        This method should be called after all route segments have been added
        to the node cache.

        """

        if parent is not None:
            nodes = self.id_to_nodes[id(obj)]
            parent_nodes = self.id_to_nodes[id(parent)]

            if nodes and parent_nodes:
                assert len(nodes & parent_nodes) > 0, (parent, obj)

        for child in obj.branches:
            self.check_tree(child, parent=obj)

    def attach(self, parent_id, child_id):
        """ Attach a child routing tree to the routing tree for parent. """
        self.id_to_obj[parent_id].branches.append(self.id_to_obj[child_id])

    def nodes_for_branch(self, obj):
        """ Return the node pkey's attached to the routing branch in obj. """
        return self.id_to_nodes[id(obj)]


def yield_branches(routing_branch):
    """ Yield all routing branches starting from the given route segment.

    This will yield the input route branch in addition to its children.

    """
    objs = set()

    def descend(obj):
        obj_id = id(obj)
        assert obj_id not in objs
        objs.add(obj_id)

        yield obj

        for seg in obj.branches:
            for s in descend(seg):
                yield s

    for s in descend(routing_branch):
        yield s


def duplicate_check(sources, stubs):
    """ Check routing sources and stubs for duplicate objects.

    Returns the total number of routing branches in the sources and stubs list.

    """
    objs = set()

    def descend(obj):
        obj_id = id(obj)
        assert obj_id not in objs

        objs.add(obj_id)

        for obj in obj.branches:
            descend(obj)

    for obj in sources:
        descend(obj)

    for obj in stubs:
        descend(obj)

    return len(objs)


def attach_candidates(node_cache, id_to_idx, stitched_stubs, objs_to_attach,
                      route_branch, visited):
    """ Attach children of branches in the routing tree route_branch.

    node_cache : NodeCache
        A node cache that contains all routing branches in the net.

    id_to_idx : dict object id to int
        Map of object id to idx in a list of unstitched routing branches.

    stitched_stubs : set of int
        Set of indicies of stubs that have been stitched.  Used to track which
        stubs have been stitched into the tree, and verify stubs are not
        stitched twice into the tree.

    objs_to_attach : list of parent object id to child object id
        When attach_candidates finds a stub that should be stitched into the
        routing tree, rather than stitch it immediately, it adds a parent of
        (id(parent), id(child)) to objs_to_attach.  This deferal enables the
        traversal of the input routing tree without modification.

        After attach_candidates returns, elements of objs_to_attach should be
        passed to node_cache.attach to join the trees.

    obj : PhysicalBelPin/PhysicalSitePin/PhysicalSitePip/PhysicalPip
        Root of routing tree to iterate over to identify candidates to attach
        to routing tree..

    visited : set of ids to routing branches.

    """
    root_obj_id = id(route_branch)
    assert root_obj_id not in id_to_idx

    for branch in yield_branches(route_branch):
        # Make sure each route branch is only visited once.
        assert id(branch) not in visited
        visited.add(id(branch))

        for node in node_cache.nodes_for_branch(branch):
            for obj_id in node_cache.node_to_ids[node]:
                if obj_id not in id_to_idx:
                    continue

                # There should never be a loop because root_obj_id should not
                # be in the id_to_idx map once it is stitched into another tree.
                assert root_obj_id != obj_id

                idx = id_to_idx[obj_id]
                assert idx not in stitched_stubs
                stitched_stubs.add(idx)
                objs_to_attach.append((id(branch), obj_id))


def attach_from_parents(node_cache, id_to_idx, parents, visited):
    """ Attach children routing tree starting from list of parent routing trees.

    node_cache : NodeCache
        A node cache that contains all routing branches in the net.

    id_to_idx : dict object id to int
        Map of object id to idx in a list of unstitched routing branches.

    parents : list of PhysicalBelPin/PhysicalSitePin/PhysicalSitePip/PhysicalPip
        Roots of routing tree to search for children trees.

    visited : set of ids to routing branches.

    Returns set of indicies to stitched stubs.

    """
    objs_to_attach = []

    stitched_stubs = set()
    for parent in parents:
        attach_candidates(
            node_cache=node_cache,
            id_to_idx=id_to_idx,
            stitched_stubs=stitched_stubs,
            objs_to_attach=objs_to_attach,
            route_branch=parent,
            visited=visited)

    for branch_id, child_id in objs_to_attach:
        # The branch_id should not be in the id_to_idx map, because it should
        # be an outstanding stub.
        assert branch_id not in id_to_idx

        # The child_id should be in the id_to_idx map, because it should be an
        # outstanding stub.
        assert child_id in id_to_idx

        node_cache.attach(branch_id, child_id)

        stitched_stubs.add(id_to_idx[child_id])
        del id_to_idx[child_id]

    # Return the newly stitched stubs, so that they form the new parent list.
    return stitched_stubs


def stitch_stubs(stubs, cursor, site_type_pins):
    """ Stitch stubs of the routing tree into trees routed from net sources. """
    sources = []

    # Verify input stubs have no loops.
    count = duplicate_check(sources, stubs)

    stitched_stubs = set()

    node_cache = NodeCache()

    # Populate the node cache and move root stubs to the sources list.
    for idx, stub in enumerate(stubs):
        if stub.is_root():
            stitched_stubs.add(idx)
            sources.append(stub)

        node_cache.add_route_branch(stub, cursor, site_type_pins)

    # Make sure all stubs appear valid before stitching.
    for stub in stubs:
        node_cache.check_tree(stub)

    # Remove root stubs now that they are in the sources list.
    for idx in sorted(stitched_stubs, reverse=True):
        del stubs[idx]

    # Create a id to idx map so that stitching can be deferred when walking
    # trees
    id_to_idx = {}
    for idx, stub in enumerate(stubs):
        assert idx not in id_to_idx
        id_to_idx[id(stub)] = idx

    # Initial set of tree parents are just the sources
    parents = sources
    stitched_stubs = set()

    # Track visited nodes, as it is expected to never visit a route branch
    # more than once.
    visited = set()

    # Continue iterating until no more stubs are stitched.
    while len(parents) > 0:
        # Starting from the parents of the current tree, add stubs the
        # descend from this set, and create a new set of parents from those
        # stubs.
        newly_stitched_stubs = attach_from_parents(node_cache, id_to_idx,
                                                   parents, visited)

        # Mark the newly stitched stubs to be removed.
        stitched_stubs |= newly_stitched_stubs

        # New set of parents using from the newly stitched stubs.
        parents = [stubs[idx] for idx in newly_stitched_stubs]

    # Remove stitched stubs from stub list
    for idx in sorted(stitched_stubs, reverse=True):
        del stubs[idx]

    # Make sure new trees are sensible.
    for source in sources:
        node_cache.check_tree(source)

    # Make sure final source and stub lists have no duplicates.
    assert count == duplicate_check(sources, stubs)

    return sources, stubs


def create_top_level_ports(top_cell, top, port_list, direction):
    """ Add top level ports to logical netlist. """
    for wire, width in make_bus(port_list):
        wire = unescape_verilog_name(wire)
        if wire in top.port_property:
            prop = top.port_property[wire]
        else:
            prop = {}

        if width is None:
            top_cell.add_port(wire, direction, property_map=prop)
            top_cell.add_net(wire)
            top_cell.connect_net_to_cell_port(wire, wire)
        else:
            top_cell.add_bus_port(
                wire, direction, start=width, end=0, property_map=prop)
            for idx in range(width + 1):
                net_name = '{}[{}]'.format(wire, idx)
                top_cell.add_net(net_name)
                top_cell.connect_net_to_cell_port(net_name, wire, idx=idx)


def output_interchange(top, capnp_folder, part, f_logical, f_physical, f_xdc):
    """ Output FPGA interchange from top level Module class object.

    top (Module) - Top level module.
    capnp_folder (str) - Path to the interchange capnp folder
    part (str) - Part for physical netlist.
    f_logical (file-like) - File to output logical_netlist.Netlist.
    f_physical (file-like) - File to output physical_netlist.PhysNetlist.

    """
    interchange = Interchange(capnp_folder)

    hdi_primitives = Library('hdi_primitives')
    work = Library('work')
    libraries = {hdi_primitives.name: hdi_primitives, work.name: work}

    top_cell = Cell(top.name)

    # Create source cells for constant nets.  They are required to have some
    # name, so give them one.
    #
    # TODO: Iterate net names on this?  This feels wrong/weird.  Need to
    # handle net name collisions?
    constant_nets = {
        0: "GLOBAL_LOGIC0",
        1: "GLOBAL_LOGIC1",
    }

    top_cell.add_cell_instance(name='VCC', cell_name="VCC")
    top_cell.add_net(constant_nets[1])
    top_cell.connect_net_to_instance(
        net_name=constant_nets[1], instance_name='VCC', port="P")

    top_cell.add_cell_instance(name='GND', cell_name="GND")
    top_cell.add_net(constant_nets[0])
    top_cell.connect_net_to_instance(
        net_name=constant_nets[0], instance_name='GND', port="G")

    # Parse top level port names, and convert to bussed ports as needed.
    create_top_level_ports(top_cell, top, top.root_in, Direction.Input)
    create_top_level_ports(top_cell, top, top.root_out, Direction.Output)
    create_top_level_ports(top_cell, top, top.root_inout, Direction.Inout)

    for wire, width in make_bus(top.wires):
        wire = unescape_verilog_name(wire)
        if width is None:
            top_cell.add_net(name=wire)
        else:
            for idx in range(width + 1):
                top_cell.add_net(name='{}[{}]'.format(wire, idx))

    # Update/create wire_name_net_map from the BELs.
    for site in top.sites:
        for bel in site.bels:
            bel.make_net_map(top=top, net_map=top.wire_name_net_map)

    for sink_wire, source_wire in top.wire_assigns.yield_wires():
        net_name = flatten_wires(source_wire, top.wire_assigns,
                                 top.wire_name_net_map)
        if sink_wire in top.wire_name_net_map:
            assert top.wire_name_net_map[sink_wire] == net_name
        else:
            top.wire_name_net_map[sink_wire] = net_name

    # Create a list of each primative instances to later build up a primative
    # model library.
    hdi_primitives_cells = {}

    # Create cells instances from each bel in the design.
    for site in top.sites:
        for bel in sorted(site.bels, key=lambda bel: bel.priority):
            bel.output_interchange(
                top_cell=top_cell,
                top=top,
                net_map=top.wire_name_net_map,
                constant_nets=constant_nets,
            )

            if bel.parent_cell is not None:
                continue

            if bel.module not in hdi_primitives_cells:
                hdi_primitives_cells[bel.module] = []

            hdi_primitives_cells[bel.module].append(bel)

    # Add top level cell to the work cell library.
    work.add_cell(top_cell)

    # Construct library cells based on data from top module.
    for cellname in hdi_primitives_cells:
        instances = hdi_primitives_cells[cellname]

        cell = Cell(cellname)

        ports = {}
        for instance in instances:
            _, connections, port_is_output = instance.create_connections(top)

            for port in connections:
                if port_is_output[port]:
                    # The current model doesn't handle IO at all, so add
                    # special cases for IO ports in the library.
                    if cellname.startswith('IOBUF') and port == "IO":
                        direction = Direction.Inout
                    else:
                        direction = Direction.Output
                else:
                    direction = Direction.Input

                width = connections[port].bus_width()
                if port in instance.port_width:
                    if width is not None:
                        assert width <= instance.port_width[port], port

                    width = instance.port_width[port]

                if port in ports:
                    port_dir, port_width = ports[port]
                    assert port_dir == direction, (port, direction, port_dir,
                                                   port_width)
                    if width is not None:
                        assert port_width <= width

                        if width > port_width:
                            ports[port] = (direction, width)
                    else:
                        assert port_width is None
                else:
                    ports[port] = (direction, width)

            # Add instances of unconnected ports (as needed).
            for port, direction in instance.port_direction.items():
                width = instance.port_width[port]

                if direction == "output":
                    direction = Direction.Output
                elif direction == "inout":
                    direction = Direction.Inout
                else:
                    assert direction == "input", direction
                    direction = Direction.Input

                if port in ports:
                    assert (direction, width) == ports[port]
                else:
                    ports[port] = (direction, width)

        for port, (direction, width) in ports.items():

            if width is not None:
                cell.add_bus_port(port, direction, start=width - 1, end=0)
            else:
                cell.add_port(port, direction)

        hdi_primitives.add_cell(cell)

    # Make sure VCC and GND primatives are in the library.
    if "VCC" not in hdi_primitives.cells:
        cell = Cell("VCC")
        cell.add_port("P", Direction.Output)

        hdi_primitives.add_cell(cell)

    if "GND" not in hdi_primitives.cells:
        cell = Cell("GND")
        cell.add_port("G", Direction.Output)

        hdi_primitives.add_cell(cell)

    # Logical netlist is complete, output to file now!
    logical_netlist = LogicalNetlist(
        name=top.name,
        property_map={},
        top_instance_name=top.name,
        top_instance=CellInstance(
            cell_name=top.name, view='netlist', property_map={}),
        libraries=libraries,
    ).convert_to_capnp(interchange)
    write_capnp_file(logical_netlist, f_logical)

    physical_netlist = PhysicalNetlist(part=part)

    site_type_pins = {}

    # Convert sites and bels into placement directives and physical nets.
    net_stubs = {}
    sub_cell_nets = {}
    for site in top.sites:
        physical_netlist.add_site_instance(site.site.name, site.site_type())

        for bel in site.bels:
            if bel.site is None or (bel.bel is None
                                    and len(bel.physical_bels) == 0):
                continue

            cell_instance = unescape_verilog_name(bel.get_cell(top))

            # bel.physical_bels is used to represent a transformation that
            # happens from the library cell (e.g. LUT6_2) into lower
            # primatives (LUT6_2 -> (LUT6, LUT5)).
            #
            # Rather than implement generic transformation support, for now
            # models implement the transformation by adding physical bels to
            # generate the correct placement constraints.
            #
            # TODO: Revisit this in the future?
            if len(bel.physical_bels) == 0:
                # Straight forward case, 1 logical Cell -> 1 physical Bel
                placement = Placement(
                    cell_type=bel.module,
                    cell_name=cell_instance,
                    site=bel.site,
                    bel=bel.bel,
                )

                for (bel_name,
                     bel_pin), cell_pin in bel.bel_pins_to_cell_pins.items():
                    placement.add_bel_pin_to_cell_pin(
                        bel_pin=bel_pin,
                        cell_pin=cell_pin,
                        bel=bel_name,
                    )

                physical_netlist.placements.append(placement)
            else:
                # Transformation cases, create a placement constraint for
                # each bel in the physical_bels list.
                #
                # These represent a cell within the primative, hence the "/"
                # when constructing the cell name.
                for phys_bel in bel.physical_bels:
                    placement = Placement(
                        cell_type=phys_bel.module,
                        cell_name=cell_instance + '/' + phys_bel.name,
                        site=bel.site,
                        bel=phys_bel.bel,
                    )

                    for (bel_name, bel_pin
                         ), cell_pin in phys_bel.bel_pins_to_cell_pins.items():
                        placement.add_bel_pin_to_cell_pin(
                            bel_pin=bel_pin,
                            cell_pin=cell_pin,
                            bel=bel_name,
                        )

                    physical_netlist.placements.append(placement)

        # Convert site routing to PhysicalNetlist objects (PhysicalBelPin,
        # PhysicalSitePin, PhysicalSitePip).
        #
        # Note: Calling output_site_routing must be done before
        # output_interchange_nets to ensure that Bel.final_net_names gets
        # populated, as that is computed during Site.output_site_routing.
        new_nets = site.output_site_routing(
            top=top,
            parent_cell=top_cell,
            net_map=top.wire_name_net_map,
            constant_nets=constant_nets,
            sub_cell_nets=sub_cell_nets)

        for site_pin, site_type_pin in site.site_type_pins.items():
            site_type_pins[site.site.name, site_pin] = site_type_pin

        # Extend net stubs with the site routing.
        for net_name in new_nets:
            if net_name not in net_stubs:
                net_stubs[net_name] = []

            net_stubs[net_name].extend(new_nets[net_name])

    # Convert top level routing nets to pip lists and to relevant nets
    for net_name, pips in top.output_interchange_nets(
            constant_nets=constant_nets):
        if net_name not in net_stubs:
            net_stubs[net_name] = []

        for tile, wire0, wire1 in pips:
            # TODO: Better handling of bipips?
            net_stubs[net_name].append(
                PhysicalPipForStitching(
                    tile=tile, wire0=wire0, wire1=wire1, forward=False))

    net_to_type = {}
    for val, net_name in constant_nets.items():
        if val == 0:
            net_to_type[net_name] = PhysicalNetType.Gnd
        else:
            assert val == 1
            net_to_type[net_name] = PhysicalNetType.Vcc

    cursor = top.conn.cursor()
    for net_name in net_stubs:
        sources = []
        stubs = net_stubs[net_name]
        sources, stubs = stitch_stubs(net_stubs[net_name], cursor,
                                      site_type_pins)

        physical_netlist.add_physical_net(
            net_name=sub_cell_nets.get(net_name, net_name),
            sources=sources,
            stubs=stubs,
            net_type=net_to_type.get(net_name, PhysicalNetType.Signal))

    phys_netlist_capnp = physical_netlist.convert_to_capnp(interchange)
    write_capnp_file(phys_netlist_capnp, f_physical)

    for l in top.output_extra_tcl():
        print(l, file=f_xdc)
