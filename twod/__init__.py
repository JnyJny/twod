"""provides two dimensional geometric objects

"""


__version__ = "0.1.4"

from .point import Point
from .rect import Rect
from .exceptions import ColinearPoints

__all__ = ["Point", "Rect", "ColinearPoints"]
