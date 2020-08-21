import enum
from collections import namedtuple


class PhysicalCellType(enum.Enum):
    Locked = 0
    Port = 1
    Gnd = 2
    Vcc = 3


Pip = namedtuple('Pip', 'tile wire0 wire1 forward')
