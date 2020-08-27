import capnp
import capnp.lib.capnp
capnp.remove_import_hook()
import os.path
from .logical_netlist import check_logical_netlist, Library, Cell, Direction
from .physical_netlist import Placement
from ..models.verilog_modeling import make_bus, flatten_wires, unescape_verilog_quote


class LogicalNetlistBuilder():
    def __init__(self, logical_netlist_schema, name, cell_count, port_count, cell_instance_count, property_map):
        self.logical_netlist_schema = logical_netlist_schema
        self.logical_netlist = self.logical_netlist_schema.Netlist.new_message()

        self.logical_netlist.name = name

        self.string_map = {}
        self.string_list = []

        self.cell_idx = 0
        self.cell_count = cell_count
        self.logical_netlist.init("cellList", cell_count)
        self.cells = self.logical_netlist.cellList

        self.port_idx = 0
        self.port_count = port_count
        self.logical_netlist.init("portList", port_count)
        self.ports = self.logical_netlist.portList

        self.cell_instance_idx = 0
        self.cell_instance_count = cell_instance_count
        self.logical_netlist.init("instList", cell_instance_count)
        self.cell_instances = self.logical_netlist.instList

        self.create_property_map(self.logical_netlist.propMap, property_map)


    def next_cell(self):
        assert self.cell_idx < self.cell_count
        cell = self.cells[self.cell_idx]
        cell_idx = self.cell_idx
        self.cell_idx += 1

        return cell_idx, cell

    def get_cell(self, cell_idx):
        return self.logical_netlist.cellList[cell_idx]

    def next_port(self):
        assert self.port_idx < self.port_count
        port = self.ports[self.port_idx]
        port_idx = self.port_idx
        self.port_idx += 1

        return port_idx, port

    def next_cell_instance(self):
        assert self.cell_instance_idx < self.cell_instance_count
        cell_instance = self.cell_instances[self.cell_instance_idx]
        cell_instance_idx = self.cell_instance_idx
        self.cell_instance_idx += 1

        return cell_instance_idx, cell_instance

    def string_id(self, s):
        if s not in self.string_map:
            self.string_map[s] = len(self.string_list)
            self.string_list.append(s)

        return self.string_map[s]

    def finish_encode(self):
        self.logical_netlist.init('strList', len(self.string_list))

        for idx, s in enumerate(self.string_list):
            self.logical_netlist.strList[idx] = s

        return self.logical_netlist

    def create_property_map(self, property_map, d):
        entries = property_map.init('entries', len(d))
        for entry, (k, v) in zip(entries, d.items()):
            assert isinstance(k, str)
            entry.key = self.string_id(k)

            if isinstance(v, str):
                if v[0] == '"' and v[-1] == '"':
                    v = v[1:-1]
                entry.textValue = self.string_id(v)
            elif isinstance(v, bool):
                entry.boolValue = v
            elif isinstance(v, int):
                entry.intValue = v
            else:
                assert False, "Unknown type of value {}, type = {}".format(repr(v), type(v))

    def get_top_cell_instance(self):
        return self.logical_netlist.topInst


def output_logical_netlist(logical_netlist_schema, libraries, top_level_cell, top_level_name, view="netlist", property_map={}):
    master_cell_list = check_logical_netlist(libraries)

    assert top_level_cell in master_cell_list

    cell_count = 0
    port_count = 0
    cell_instance_count = 0
    for lib in libraries.values():
        cell_count += len(lib.cells)
        for cell in lib.cells.values():
            port_count += len(cell.ports)
            cell_instance_count += len(cell.cell_instances)

    logical_netlist = LogicalNetlistBuilder(
            logical_netlist_schema=logical_netlist_schema,
            name=top_level_name,
            cell_count=cell_count,
            port_count=port_count,
            cell_instance_count=cell_instance_count,
            property_map=property_map)

    cell_name_to_idx = {}
    ports = {}

    for library, lib in libraries.items():
        library_id = logical_netlist.string_id(library)
        for cell in lib.cells.values():
            cell_idx, cell_obj = logical_netlist.next_cell()
            assert cell.name not in cell_name_to_idx
            cell_name_to_idx[cell.name] = cell_idx

            cell_obj.name = logical_netlist.string_id(cell.name)
            logical_netlist.create_property_map(cell_obj.propMap, cell.property_map)
            cell_obj.view = logical_netlist.string_id(cell.view)
            cell_obj.lib = library_id

            cell_obj.init('ports', len(cell.ports))
            for idx, (port_name, port) in enumerate(cell.ports.items()):
                port_idx, port_obj = logical_netlist.next_port()
                ports[cell.name, port_name] = port_idx
                cell_obj.ports[idx] = port_idx

                port_obj.dir = logical_netlist_schema.Netlist.Direction.__dict__[port.direction.name.lower()]
                logical_netlist.create_property_map(port_obj.propMap, port.property_map)
                if port.bus is not None:
                    port_obj.name = logical_netlist.string_id(port_name)
                    bus = port_obj.init('bus')
                    bus.busStart = port.bus.start
                    bus.busEnd = port.bus.end
                else:
                    port_obj.name = logical_netlist.string_id(port_name)
                    port_obj.bit = None

    for lib in libraries.values():
        for cell in lib.cells.values():
            cell_obj = logical_netlist.get_cell(cell_name_to_idx[cell.name])

            cell_instances = {}
            cell_obj.init('insts', len(cell.cell_instances))
            for idx, (cell_instance_name, cell_instance) in enumerate(cell.cell_instances.items()):
                cell_instance_idx, cell_instance_obj = logical_netlist.next_cell_instance()
                cell_instances[cell_instance_name] = cell_instance_idx

                cell_instance_obj.name = logical_netlist.string_id(cell_instance_name)
                logical_netlist.create_property_map(cell_instance_obj.propMap, cell_instance.property_map)
                cell_instance_obj.view = logical_netlist.string_id(cell_instance.view)
                cell_instance_obj.cell = cell_name_to_idx[cell_instance.cell_name]

                cell_obj.insts[idx] = cell_instance_idx

            cell_obj.init('nets', len(cell.nets))
            for net_obj, (netname, net) in zip(cell_obj.nets, cell.nets.items()):
                net_obj.name = logical_netlist.string_id(netname)
                logical_netlist.create_property_map(net_obj.propMap, net.property_map)

                net_obj.init('portInsts', len(net.ports))

                for port_obj, port in zip(net_obj.portInsts, net.ports):
                    if port.instance_name is not None:
                        instance_cell_name = cell.cell_instances[port.instance_name].cell_name
                        port_obj.inst = cell_instances[port.instance_name]
                        port_obj.port = ports[instance_cell_name, port.name]
                    else:
                        port_obj.extPort = None
                        port_obj.port = ports[cell.name, port.name]

                    if port.idx is not None:
                        port_obj.busIdx.idx = port.idx
                    else:
                        port_obj.busIdx.singleBit = None

    top_level_cell_instance = logical_netlist.get_top_cell_instance()

    top_level_cell_instance.name = logical_netlist.string_id(top_level_name)
    top_level_cell_instance.cell = cell_name_to_idx[top_level_cell]
    top_level_cell_instance.view = logical_netlist.string_id(view)
    logical_netlist.create_property_map(top_level_cell_instance.propMap, property_map)

    return logical_netlist.finish_encode()


class PhysicalNetlistBuilder():
    def __init__(self, physical_netlist_schema, part):
        self.physical_netlist_schema = physical_netlist_schema

        self.physical_netlist = self.physical_netlist_schema.PhysNetlist.new_message()
        self.physical_netlist.part = part

        self.placements = []
        self.nets = []
        self.physical_cells = []
        self.site_instances = {}
        self.properties = {}

        self.string_map = {}
        self.string_list = []

    def add_physical_cell(self, cell_name, cell_type):
        self.physical_cells.append((cell_name, cell_type))

    def add_cell_loc(self, placement):
        self.placements.append(placement)

    def add_physical_net(self, net_name, roots, stubs):
        self.nets.append((net_name, roots, stubs))

    def string_id(self, s):
        if s not in self.string_map:
            self.string_map[s] = len(self.string_list)
            self.string_list.append(s)

        return self.string_map[s]

    def finish_encode(self):
        self.physical_netlist.init('placements', len(self.placements))
        placements = self.physical_netlist.placements
        for idx, placement in enumerate(self.placements):
            placement_obj = placements[idx]

            placement_obj.cellName = self.string_id(placement.cell_name)
            placement_obj.type = self.string_id(placement.cell_type)

            placement_obj.site = self.string_id(placement.site)
            placement_obj.bel = self.string_id(placement.bel)
            placement_obj.isSiteFixed = True
            placement_obj.isBelFixed = True

            if placement.other_bels:
                placement_obj.init('otherBels', len(placement.other_bels))
                other_bels_obj = placement_obj.otherBels
                for idx, s in enumerate(placement.other_bels):
                    other_bels_obj[idx] = self.string_id(s)

            placement_obj.init('pinMap', len(placement.pins))
            pin_map = placement_obj.pinMap
            for idx, pin in enumerate(placement.pins):
                pin_map[idx].cellPin = self.string_id(pin.cell_pin)
                pin_map[idx].belPin = self.string_id(pin.bel_pin)
                if pin.bel is None:
                    pin_map[idx].bel = placement_obj.bel
                else:
                    pin_map[idx].bel = self.string_id(pin.bel)
                pin_map[idx].isFixed = True

                if pin.other_cell_type:
                    assert pin.other_cell_name is not None
                    pin.otherCell.multiCell = self.string_id(pin.other_cell_name)
                    pin.otherCell.multiType = self.string_id(pin.other_cell_type)

        self.physical_netlist.init('physNets', len(self.nets))
        nets = self.physical_netlist.physNets
        for idx, (net_name, roots, stubs) in enumerate(self.nets):
            net = nets[idx]

            net.name = self.string_id(net_name)
            net.init('sources', len(roots))
            for root_obj, root in zip(net.sources, roots):
                root.output_interchange(root_obj, self.string_id)

            net.init('stubs', len(stubs))
            for stub_obj, stub in zip(net.stubs, stubs):
                stub.output_interchange(stub_obj, self.string_id)

        self.physical_netlist.init('physCells', len(self.physical_cells))
        physical_cells = self.physical_netlist.physCells
        for idx, (cell_name, cell_type) in enumerate(self.physical_cells):
            physical_cell = physical_cells[idx]
            physical_cell.cellName = self.string_id(cell_name)
            physical_cell.physType = self.physical_netlist_schema.PhysNetlist.PhysCellType.__dict__[cell_type.name.lower()]

        self.physical_netlist.init('properties', len(self.properties))
        properties = self.physical_netlist.properties
        for idx, (k, v) in enumerate(self.properties.items()):
            properties[idx].key = self.string_id(k)
            properties[idx].value = self.string_id(v)

        self.physical_netlist.init('siteInsts', len(self.site_instances))
        site_instances = self.physical_netlist.siteInsts
        for idx, (k, v) in enumerate(self.site_instances.items()):
            site_instances[idx].site = self.string_id(k)
            site_instances[idx].type = self.string_id(v)

        self.physical_netlist.init('strList', len(self.string_list))

        for idx, s in enumerate(self.string_list):
            self.physical_netlist.strList[idx] = s

        return self.physical_netlist


class Interchange():
    def __init__(self, schema_directory):
        self.logical_netlist_schema = capnp.load(
                os.path.join(schema_directory, 'LogicalNetlist.capnp'),
                imports=[os.path.dirname(os.path.dirname(capnp.__file__))]
                )
        self.physical_netlist_schema = capnp.load(
                os.path.join(schema_directory, 'PhysicalNetlist.capnp'),
                imports=[os.path.dirname(os.path.dirname(capnp.__file__))]
                )

    def output_logical_netlist(self, *args, **kwargs):
        return output_logical_netlist(logical_netlist_schema=self.logical_netlist_schema, *args, **kwargs)

    def new_physical_netlist_builder(self, *args, **kwargs):
        return PhysicalNetlistBuilder(physical_netlist_schema=self.physical_netlist_schema, *args, **kwargs)


def output_interchange(top, capnp_folder, part, f_logical, f_physical):
    interchange = Interchange(capnp_folder)

    hdi_primitives = Library('hdi_primitives')
    work = Library('work')
    libraries = {
            hdi_primitives.name: hdi_primitives,
            work.name: work
            }

    top_cell = Cell(top.name)

    # TODO: Iterate on this?  This feels wrong/weird.
    top_cell.add_cell_instance(
            name='VCC',
            cell_name="VCC")
    top_cell.add_net('<const1>')
    top_cell.connect_net_to_instance(
            net_name='<const1>',
            instance_name='VCC',
            port="P")

    top_cell.add_cell_instance(
            name='GND',
            cell_name="GND")
    top_cell.add_net('<const0>')
    top_cell.connect_net_to_instance(
            net_name='<const0>',
            instance_name='GND',
            port="G")

    constant_nets = {
            0: "<const0>",
            1: "<const1>",
            }

    for in_wire, width in make_bus(top.root_in):
        in_wire = unescape_verilog_quote(in_wire)
        if in_wire in top.port_property:
            prop = top.port_property[in_wire]
        else:
            prop = {}

        if width is None:
            top_cell.add_port(in_wire, Direction.Input, property_map=prop)
            top_cell.add_net(in_wire)
            top_cell.connect_net_to_cell_port(in_wire, in_wire)
        else:
            top_cell.add_bus_port(in_wire, Direction.Input, start=0, end=width, property_map=prop)
            for idx in range(width+1):
                net_name = '{}[{}]'.format(in_wire, idx)
                top_cell.add_net(net_name)
                top_cell.connect_net_to_cell_port(net_name, in_wire, idx=idx)


    for out_wire, width in make_bus(top.root_out):
        out_wire = unescape_verilog_quote(out_wire)
        if out_wire in top.port_property:
            prop = top.port_property[out_wire]
        else:
            prop = {}

        if width is None:
            top_cell.add_port(out_wire, Direction.Output, property_map=prop)
            top_cell.add_net(out_wire)
            top_cell.connect_net_to_cell_port(out_wire, out_wire)
        else:
            top_cell.add_bus_port(out_wire, Direction.Output, start=0, end=width, property_map=prop)
            for idx in range(width+1):
                net_name = '{}[{}]'.format(out_wire, idx)
                top_cell.add_net(net_name)
                top_cell.connect_net_to_cell_port(net_name, out_wire, idx=idx)

    for inout_wire, width in make_bus(top.root_inout):
        inout_wire = unescape_verilog_quote(inout_wire)
        if inout_wire in top.port_property:
            prop = top.port_property[inout_wire]
        else:
            prop = {}

        if width is None:
            top_cell.add_port(inout_wire, Direction.Inout, property_map=prop)
            top_cell.add_net(inout_wire)
            top_cell.connect_net_to_cell_port(inout_wire, inout_wire)
        else:
            top_cell.add_bus_port(inout_wire, Direction.Inout, start=0, end=width, property_map=prop)
            for idx in range(width+1):
                net_name = '{}[{}]'.format(inout_wire, idx)
                top_cell.add_net(net_name)
                top_cell.connect_net_to_cell_port(net_name, inout_wire, idx=idx)

    for wire, width in make_bus(top.wires):
        wire = unescape_verilog_quote(wire)
        if width is None:
            top_cell.add_net(name=wire)
        else:
            for idx in range(width+1):
                top_cell.add_net(name='{}[{}]'.format(wire, idx))

    for site in top.sites:
        for bel in site.bels:
            bel.make_net_map(top=top, net_map=top.wire_name_net_map)

    for sink_wire, source_wire in top.wire_assigns.yield_wires():
        top.wire_name_net_map[sink_wire] = flatten_wires(
            source_wire, top.wire_assigns, top.wire_name_net_map)

    hdi_primitives_cells = {}

    for site in top.sites:
        for bel in sorted(site.bels, key=lambda bel: bel.priority):
            bel.output_interchange(
                top_cell=top_cell,
                top=top,
                net_map=top.wire_name_net_map,
                constant_nets=constant_nets,
                )

            if bel.module not in hdi_primitives_cells:
                hdi_primitives_cells[bel.module] = []

            hdi_primitives_cells[bel.module].append(bel)

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
                    if cellname.startswith('IOBUF') and port == "IO":
                        direction = Direction.Inout
                    else:
                        direction = Direction.Output
                else:
                    direction = Direction.Input

                width = connections[port].bus_width()

                if port in ports:
                    port_dir, port_width = ports[port]
                    assert port_dir == direction
                    if width is not None:
                        assert port_width <= width

                        if width > port_width:
                            ports[port] = (direction, width)
                    else:
                        assert port_width is None
                else:
                    ports[port] = (direction, width)

        for port, (direction, width) in ports.items():

            if width is not None:
                cell.add_bus_port(port, direction, start=0, end=width-1)
            else:
                cell.add_port(port, direction)

        hdi_primitives.add_cell(cell)

    if "VCC" not in hdi_primitives.cells:
        cell = Cell("VCC")
        cell.add_port("P", Direction.Output)

        hdi_primitives.add_cell(cell)

    if "GND" not in hdi_primitives.cells:
        cell = Cell("GND")
        cell.add_port("G", Direction.Output)

        hdi_primitives.add_cell(cell)

    logical_netlist = interchange.output_logical_netlist(
            libraries=libraries,
            top_level_cell=top.name,
            top_level_name=top.name)
    logical_netlist.write_packed(f_logical)

    physical_netlist_builder = interchange.new_physical_netlist_builder(part=part)

    net_stubs = {}
    for site in top.sites:
        physical_netlist_builder.site_instances[site.site.name] = site.site_type()

        for bel in site.bels:
            if bel.site is None or bel.bel is None or bel.no_place:
                continue

            cell_instance = unescape_verilog_quote(bel.get_cell(top))

            if len(bel.physical_bels) == 0:
                placement = Placement(
                        cell_type=bel.module,
                        cell_name=cell_instance,
                        site=bel.site,
                        bel=bel.bel,
                        )

                for (bel_name, bel_pin), cell_pin in bel.bel_pins_to_cell_pins.items():
                    placement.add_bel_pin_to_cell_pin(
                            bel_pin=bel_pin,
                            cell_pin=cell_pin,
                            bel=bel_name,
                            )

                physical_netlist_builder.placements.append(placement)
            else:
                for phys_bel in bel.physical_bels:
                    placement = Placement(
                            cell_type=phys_bel.module,
                            cell_name=cell_instance + '/' + phys_bel.name,
                            site=bel.site,
                            bel=phys_bel.bel,
                            )

                    for (bel_name, bel_pin), cell_pin in phys_bel.bel_pins_to_cell_pins.items():
                        placement.add_bel_pin_to_cell_pin(
                                bel_pin=bel_pin,
                                cell_pin=cell_pin,
                                bel=bel_name,
                                )

                    physical_netlist_builder.placements.append(placement)


        new_nets = site.output_site_routing(
                top=top,
                parent_cell=top_cell,
                net_map=top.wire_name_net_map,
                constant_nets=constant_nets)

        for net_name in new_nets:
            if net_name not in net_stubs:
                net_stubs[net_name] = []

            net_stubs[net_name].extend(new_nets[net_name])

    for net_name in net_stubs:
        physical_netlist_builder.add_physical_net(
                net_name=net_name,
                roots=[],
                stubs=net_stubs[net_name],
                )

    physical_netlist = physical_netlist_builder.finish_encode()
    physical_netlist.write_packed(f_physical)
