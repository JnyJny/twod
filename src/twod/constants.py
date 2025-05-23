"""geometric constants for humans™"""

from enum import Enum, IntEnum, auto


class Quadrant(int, Enum):
    ORIGIN = auto()
    I = auto()
    II = auto()
    III = auto()
    IV = auto()


EPSILON_EXP_MINUS_1 = 15
