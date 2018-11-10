"""provides two dimensional geometric objects

"""


__version__ = "0.1.3"

from .point import Point
from .rect import Rect
from .exceptions import ColinearPoints

__all__ = ["Point", "Rect", "ColinearPoints"]
