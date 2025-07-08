"""two-dimensional geometric objects for humans™"""

from .constants import Quadrant
from .cpoint import CPoint
from .crect import CRect
from .exceptions import ColinearPoints
from .point import Point
from .rect import Rect

__all__ = [
    "ColinearPoints",
    "CPoint",
    "CRect",
    "Point",
    "Quadrant",
    "Rect",
]
