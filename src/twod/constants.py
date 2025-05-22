"""geometric constants for humans™
"""

from enum import IntEnum


class Quadrant(IntEnum):
    ORIGIN: int = -1
    I: int = 0
    II: int = 1
    III: int = 2
    IV: int = 3


EPSILON_EXP_MINUS_1 = 15
