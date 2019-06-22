""" twod typing hinting for humans™.
"""

from typing import TypeVar, Union, Tuple

Numeric = Union[float, int]
Coordinate = Tuple[Numeric, Numeric]
PointOrScalar = TypeVar("PointOrScalar")
PointType = TypeVar("PointType")
