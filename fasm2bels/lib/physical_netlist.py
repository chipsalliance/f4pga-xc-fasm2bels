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

    def add_bel_pin_to_cell_pin(self, bel_pin, cell_pin, bel=None, other_cell_type=None, other_cell_name=None):
        if bel != self.bel:
            self.other_bels.add(bel)

        self.pins.append(Pin(
            bel_pin=bel_pin,
            cell_pin=cell_pin,
            bel=bel,
            other_cell_type=other_cell_type,
            other_cell_name=other_cell_name,
            ))
