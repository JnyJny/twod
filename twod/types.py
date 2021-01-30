""" twod typing hinting for humans™.
"""

from typing import Iterable, TypeVar, Union

Numeric = Union[float, int]

PointType = TypeVar("PointType")
PointOrScalar = Union[PointType, Numeric]
PointOrIterable = Union[PointType, Iterable[Numeric]]
PointOrIterableOrScalar = Union[PointType, Iterable[Numeric], Numeric]
