"""geometric constants for humans™"""

from enum import Enum, auto


class Quadrant(int, Enum):
    ORIGIN = auto()
    FIRST = auto()
    SECOND = auto()
    THIRD = auto()
    FOURTH = auto()
    X_AXIS = auto()
    Y_AXIS = auto()


class Winding(int, Enum):
    CW = auto()
    CCW = auto()
    Colinear = auto()


EPSILON_EXP_MINUS_1 = 15
