"""two-dimensional geometric objects for humans™"""

from .constants import Quadrant
from .cpoint import CPoint
from .crect import CRect
from .exceptions import ColinearPoints
from .line import Line
from .point import Point
from .rect import Rect

__all__ = [
    "ColinearPoints",
    "CPoint",
    "CRect",
    "Line",
    "Point",
    "Quadrant",
    "Rect",
]
