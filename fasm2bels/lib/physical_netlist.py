import enum
from collections import namedtuple


class PhysicalCellType(enum.Enum):
    Locked = 0
    Port = 1
    Gnd = 2
    Vcc = 3


Pip = namedtuple('Pip', 'tile wire0 wire1 forward')

Pin = namedtuple('Pin', 'bel_pin cell_pin bel other_cell_type other_cell_name')


class Placement():
    def __init__(self, cell_type, cell_name, site, bel):
        self.cell_type = cell_type
        self.cell_name = cell_name

        self.site = site
        self.bel = bel

        self.pins = []
        self.other_bels = set()

    def add_bel_pin_to_cell_pin(self,
                                bel_pin,
                                cell_pin,
                                bel=None,
                                other_cell_type=None,
                                other_cell_name=None):
        if bel != self.bel:
            self.other_bels.add(bel)

        self.pins.append(
            Pin(
                bel_pin=bel_pin,
                cell_pin=cell_pin,
                bel=bel,
                other_cell_type=other_cell_type,
                other_cell_name=other_cell_name,
            ))


def descend_branch(obj, node, string_id):
    obj.init('branches', len(node.branches))

    for branch_obj, branch in zip(obj.branches, node.branches):
        branch.output_interchange(branch_obj, string_id)


class PhysicalBelPin():
    def __init__(self, site, bel, pin):
        self.site = site
        self.bel = bel
        self.pin = pin

        self.branches = []

    def output_interchange(self, obj, string_id):
        obj.routeSegment.init('belPin')
        obj.routeSegment.belPin.site = string_id(self.site)
        obj.routeSegment.belPin.bel = string_id(self.bel)
        obj.routeSegment.belPin.pin = string_id(self.pin)

        descend_branch(obj, self, string_id)


class PhysicalSitePin():
    def __init__(self, site, pin):
        self.site = site
        self.pin = pin

        self.branches = []

    def output_interchange(self, obj, string_id):
        obj.routeSegment.init('sitePin')
        obj.routeSegment.sitePin.site = string_id(self.site)
        obj.routeSegment.sitePin.pin = string_id(self.pin)

        descend_branch(obj, self, string_id)


class PhysicalPip():
    def __init__(self, tile, wire0, wire1, forward):
        self.tile = tile
        self.wire0 = wire0
        self.wire1 = wire1
        self.forward = forward

        self.branches = []

    def output_interchange(self, obj, string_id):
        obj.routeSegment.init('pip')
        obj.routeSegment.pip.tile = string_id(self.tile)
        obj.routeSegment.pip.wire0 = string_id(self.wire0)
        obj.routeSegment.pip.wire1 = string_id(self.wire1)
        obj.routeSegment.pip.forward = self.forward
        obj.routeSegment.pip.isFixed = True

        descend_branch(obj, self, string_id)


class PhysicalSitePip():
    def __init__(self, site, bel, pin):
        self.site = site
        self.bel = bel
        self.pin = pin

        self.branches = []

    def output_interchange(self, obj, string_id):
        obj.routeSegment.init('sitePIP')
        obj.routeSegment.sitePIP.site = string_id(self.site)
        obj.routeSegment.sitePIP.bel = string_id(self.bel)
        obj.routeSegment.sitePIP.pin = string_id(self.pin)

        descend_branch(obj, self, string_id)


def convert_tuple_to_object(site, tup):
    if tup[0] == 'site_pin':
        _, pin = tup
        return PhysicalSitePin(site.name, pin)
    elif tup[0] == 'bel_pin':
        _, bel, pin = tup
        return PhysicalBelPin(site.name, bel, pin)
    elif tup[0] == 'site_pip':
        _, bel, pin = tup
        return PhysicalSitePip(site.name, bel, pin)
    else:
        assert False, tup


def add_site_routing_children(site, root_obj, root_key, site_routing,
                              inverted_root):
    if root_key in site_routing:
        for child in site_routing[root_key]:
            if child[0] == 'inverter' and inverted_root is not None:
                for child2 in site_routing[child]:
                    obj = convert_tuple_to_object(site, child2)
                    inverted_root.append(obj)
            else:
                obj = convert_tuple_to_object(site, child)
                root_obj.branches.append(obj)

                add_site_routing_children(site, obj, child, site_routing,
                                          inverted_root)


def create_site_routing(site, net_roots, site_routing, constant_nets):
    nets = {}

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
