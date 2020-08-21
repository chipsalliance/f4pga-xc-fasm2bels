import enum
from collections import namedtuple

class Direction(enum.Enum):
    Input = 0
    Output = 1
    Inout = 2

Bus = namedtuple('Bus', 'start end')

Port = namedtuple('Port', 'direction property_map bus')

PortInstance = namedtuple('PortInstance', 'name instance_name idx')

Net = namedtuple('Net', 'name property_map ports')

CellInstance = namedtuple('CellInstance', 'property_map view cell_name')

Cell = namedtuple('Cell', 'name property_map view lib cell_instances nets ports')


class Cell():
    def __init__(self, name, property_map={}):
        self.name = name
        self.property_map = property_map
        self.view = "netlist"

        self.nets = {}
        self.ports = {}
        self.cell_instances = {}

    def add_port(self, name, direction, property_map={}):
        assert name not in self.ports

        self.ports[name] = Port(
                direction=direction,
                property_map=property_map,
                bus=None)

    def add_bus_port(self, name, direction, start, end, property_map={}):
        assert name not in self.ports
        self.ports[name] = Port(
                direction=direction,
                property_map=property_map,
                bus=Bus(start=start, end=end))

    def add_cell_instance(self, name, cell_name, property_map={}):
        assert name not in self.cell_instances
        self.cell_instances[name] = CellInstance(
                property_map=property_map,
                view="netlist",
                cell_name=cell_name)

    def add_net(self, name, property_map={}):
        assert name not in self.nets
        self.nets[name] = Net(name=name, property_map=property_map, ports=[])

    def connect_net_to_instance(self, net_name, instance_name, port, idx=None):
        assert instance_name in self.cell_instances
        port = PortInstance(name=port, instance_name=instance_name, idx=idx)
        self.nets[net_name].ports.append(port)

    def connect_net_to_cell_port(self, net_name, port, idx=None):
        assert port in self.ports
        port = PortInstance(name=port, idx=idx, instance_name=None)
        self.nets[net_name].ports.append(port)


def invert_direction(direction):
    if direction == Direction.Input:
        return Direction.Output
    elif direction == Direction.Output:
        return Direction.Input
    else:
        assert direction == Direction.Inout
        return Direction.Inout


class Library():
    def __init__(self, name):
        self.name = name
        self.cells = {}

    def add_cell(self, cell):
        assert cell.name not in self.cells
        self.cells[cell.name] = cell

def check_logical_netlist(libraries):
    master_cell_list = {}

    for lib in libraries.values():
        for cell in lib.cells.values():
            master_cell_list[cell.name] = cell

    for cell in master_cell_list.values():
        for inst in cell.cell_instances.values():
            assert inst.cell_name in master_cell_list

        for netname, net in cell.nets.items():
            port_directions = {
                    Direction.Input: 0,
                    Direction.Output: 0,
                    Direction.Inout: 0,
                    }

            for port in net.ports:
                if port.instance_name is not None:
                    # This port connects to a cell instance, go find the
                    # master cell and port.
                    instance_cell_name = cell.cell_instances[port.instance_name].cell_name
                    instance_cell = master_cell_list[instance_cell_name]
                    instance_port = instance_cell.ports[port.name]

                    net_direction = invert_direction(instance_port.direction)
                else:
                    instance_port = cell.ports[port.name]

                    net_direction = instance_port.direction

                # Count port directions on this net
                port_directions[net_direction] += 1

                # Check bus index is valid is present
                if port.idx is not None:
                    assert instance_port.bus is not None

                    assert port.idx >= instance_port.bus.start
                    assert port.idx <= instance_port.bus.end
                else:
                    assert instance_port.bus is None, (netname, port)

            if port_directions[Direction.Inout] == 0:
                assert port_directions[Direction.Input] in [0, 1], (netname, port_directions)
            else:
                # TODO: Not sure how to handle this case?
                # Should only have 0 input?
                assert port_directions[Direction.Input] == 0

    return master_cell_list.keys()
