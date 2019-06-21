"""two-dimensional geometric objects for humans™

"""

__version__ = "0.1.7"

from .point import Point
from .constants import Quadrant
from .rect import Rect
from .exceptions import ColinearPoints

__all__ = [
    "ColinearPoints",
    "Point",
    "Quadrant",
    "Rect",
]
