"""two-dimensional geometric objects for humans™"""

import importlib
import warnings
from typing import TYPE_CHECKING, Any

from .centered import Centered
from .constants import Quadrant
from .ellipse import Circle, Ellipse
from .exceptions import ColinearPoints
from .line import Line
from .point import Point
from .rect import Rect

if TYPE_CHECKING:
    from .cpoint import CPoint
    from .crect import CRect

__all__ = [
    "Centered",
    "ColinearPoints",
    "Circle",
    "Ellipse",
    "Line",
    "Point",
    "Quadrant",
    "Rect",
]

_DEPRECATED = {
    "CPoint": ("cpoint", "Point"),
    "CRect": ("crect", "Rect"),
}


def __getattr__(name: str) -> Any:
    """Import CPoint and CRect on demand, warning that they are deprecated."""
    if name in _DEPRECATED:
        module, replacement = _DEPRECATED[name]
        warnings.warn(
            f"twod.{name} is deprecated and will be removed in 0.5.0; "
            f"use twod.{replacement}",
            DeprecationWarning,
            stacklevel=2,
        )
        return getattr(importlib.import_module(f".{module}", __name__), name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
