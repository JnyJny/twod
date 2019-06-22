"""two-dimensional geometric objects for humans™

"""

__version__ = "0.1.7"

from .constants import Quadrant
from .exceptions import ColinearPoints
from .point import Point
from .rect import Rect

__all__ = [__version__, "ColinearPoints", "Point", "Quadrant", "Rect"]
