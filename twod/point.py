""" a two-dimensional point for humans™.
"""

import math
import operator
import sys

from dataclasses import dataclass
from typing import Callable, Iterable, Tuple, Union

from .types import Numeric
from .types import PointType
from .types import PointOrIterable
from .types import PointOrIterableOrScalar

from .constants import EPSILON_EXP_MINUS_1, Quadrant
from .exceptions import ColinearPoints


@dataclass
class Point:
    x: float = 0
    y: float = 0
    """A two dimensional geometric point.

    The Point class represents a geometric point with 'x' and 'y' attributes
    and has many helpful properties and methods.

    >>> p = Point()
    >>> p.is_origin
    True
    """

    @classmethod
    def from_polar(
        cls,
        radius: float,
        theta: float,
        is_radians: bool = True,
        translate: PointType = None,
    ) -> PointType:
        """Returns a Point with polar coordinates (R, ϴ).

        The point is genrated relative to the origin.

        :param float radius:
        :param float theta:
        :param bool is_radians:
        :return: Point
        """
        theta = theta if is_radians else math.radians(theta)
        point = cls()
        point.polar = (radius, theta)
        if translate:
            point += translate
        return point

    @property
    def is_origin(self) -> bool:
        """True if and only if x == 0 and y == 0."""
        return self.x == 0 and self.y == 0

    @property
    def quadrant(self) -> Quadrant:
        """The quadrant in the cartesian plane this point is located in.

        Possible values are:
        - Quadrant.I
        - Quadrant.II
        - Quadrant.III
        - Quadrant.IV
        - Quadrant.ORIGIN.
        """

        if self.x > 0:
            if self.y > 0:
                return Quadrant.I
            if self.y < 0:
                return Quadrant.IV
        if self.x < 0:
            if self.y > 0:
                return Quadrant.II
            if self.y < 0:
                return Quadrant.III

        return Quadrant.ORIGIN

    def _polar_to_cartesian(self, radius: float, radians: float) -> None:
        """Computes cartesian coordinates from polar coordinates.

        The polar coordinates are expected to be a dimensionless radius
        and angle in radians.

        :param float radius:
        :param float radians:
        """
        self.x = round(radius * math.cos(radians), EPSILON_EXP_MINUS_1)
        self.y = round(radius * math.sin(radians), EPSILON_EXP_MINUS_1)

    @property
    def radius(self) -> float:
        """The distance from this point to the origin."""
        return math.hypot(self.x, self.y)

    @radius.setter
    def radius(self, new_value: float) -> None:
        self._polar_to_cartesian(new_value, self.radians)

    @property
    def radians(self) -> float:
        """The angle in radians measured counter-clockwise from 3 o'clock."""
        return math.atan2(self.y, self.x)

    @radians.setter
    def radians(self, new_value: float) -> None:
        self._polar_to_cartesian(self.radius, new_value)

    @property
    def degrees(self) -> float:
        """The angle in degrees measured counter-clockwise from 3 o'clock."""
        return math.degrees(self.radians)

    @degrees.setter
    def degrees(self, new_value: float) -> None:
        self._polar_to_cartesian(self.radius, math.radians(new_value))

    @property
    def polar(self) -> Tuple[float, float]:
        """Polar coordinates tuple: (R, ϴ).

        R is the distance from the origin to this point.
        ϴ is the angle (radians) measured counter-clockwise from 3 o'clock.
        """
        return (self.radius, self.radians)

    @polar.setter
    def polar(self, new_values: Iterable[Numeric]) -> None:
        try:
            radius, radians, *_ = map(float, new_values)
            self._polar_to_cartesian(radius, radians)
            return
        except (TypeError, ValueError):
            pass

        raise TypeError(
            f"Expected a Iterable[Union[int, float]], got {type(new_values)}"
        )

    @property
    def polar_deg(self) -> Tuple[float, float]:
        """Polar coordinates tuple: (R, ϴ).

        R is the distance from the origin to this point.
        ϴ is the angle (degrees) measured counter-clockwise from 3 o'clock.
        """
        radius, radians = self.polar
        return (radius, math.degrees(radians))

    @polar_deg.setter
    def polar_deg(self, new_values: Tuple[Numeric, Numeric]) -> None:
        try:
            radius, degrees, *_ = map(float, new_values)
            self._polar_to_cartesian(radius=radius, radians=math.radians(degrees))
            return
        except (TypeError, ValueError):
            pass
        raise TypeError(
            f"Expected a Iterable[Union[int, float]], got {type(new_values)}"
        )

    @property
    def xy(self) -> Tuple[float, float]:
        """A tuple of this point's x and y coordinates."""
        return (self.x, self.y)

    @xy.setter
    def xy(self, new_values: Iterable[Numeric]) -> None:
        try:
            self.x, self.y, *_ = map(float, new_values)
            return
        except (TypeError, ValueError):
            pass
        raise TypeError(
            f"Expected a Iterable[Union[int, float]], got {type(new_values)}"
        )

    def __iter__(self) -> Iterable[Tuple[float, float]]:
        """An iterator over x and y coordinates."""
        return iter([self.x, self.y])

    def __len__(self) -> int:
        return 2

    def __eq__(self, other: PointOrIterable) -> bool:

        try:
            return self.x == other.x and self.y == other.y
        except AttributeError:
            pass

        return all(a == b for a, b in zip(self, other))

    def __getitem__(self, key: Union[int, slice]) -> float:

        if isinstance(key, int):
            if key == 0:
                return self.x
            if key == 1:
                return self.y
            raise IndexError("key out of range: {key}")

        if isinsance(key, slice):
            return [self.x, self.y][key]

        raise TypeError(f"Expected int or slice, not {type(key)}")

    def __setitem__(self, key: int, value: Numeric):
        if key == 0:
            self.x = value
            return
        if key == 1:
            self.y = value
            return
        raise IndexError(f"key out of range: {key}")

    def __op(self, other: PointOrIterableOrScalar, op: Callable) -> PointType:
        """"""

        try:
            return Point(op(self.x, other.x), op(self.y, other.y))
        except AttributeError:
            pass
        try:
            return Point(*[op(a, b) for a, b in zip(self, other)])
        except TypeError:
            pass
        return Point(op(self.x, other), op(self.y, other))

    def __iop(self, other: PointOrIterableOrScalar, op: Callable) -> PointType:
        """"""
        try:
            self.x = op(self.x, other.x)
            self.y = op(self.y, other.y)
            return self
        except AttributeError:
            pass

        try:
            self.x = op(self.x, other[0])
            self.y = op(self.y, other[1])
            return self
        except TypeError:
            pass

        self.x = op(self.x, other)
        self.y = op(self.y, other)
        return self

    def __add__(self, other: PointOrIterableOrScalar) -> PointType:
        """Add `other` to `self` and return a new Point."""
        return self.__op(other, operator.add)

    def __iadd__(self, other: PointOrIterableOrScalar) -> PointType:
        """Add `other` to `self` in-place and returns `self`."""
        return self.__iop(other, operator.add)

    def __sub__(self, other: PointOrIterableOrScalar) -> PointType:
        """Subtract `other` from `self` and return a new Point."""
        return self.__op(other, operator.sub)

    def __isub__(self, other: PointOrIterableOrScalar) -> PointType:
        """Subtract `other` from `self` in-place and return `self`."""
        return self.__iop(other, operator.sub)

    def __mul__(self, other: PointOrIterableOrScalar) -> PointType:
        """Multiply `self` with `other` and return a new Point."""
        return self.__op(other, operator.mul)

    def __imul__(self, other: PointOrIterableOrScalar) -> PointType:
        """Multiply `self` with `other` in-place and return `self`."""
        return self.__iop(other, operator.mul)

    def __truediv__(self, other: PointOrIterableOrScalar) -> PointType:
        """Divide `self` by `other` and return a new Point."""
        return self.__op(other, operator.truediv)

    def __itruediv__(self, other: PointOrIterableOrScalar) -> PointType:
        """Divide `self` by `other` in-place and return `self`."""
        return self.__iop(other, operator.truediv)

    def __floordiv__(self, other: PointOrIterableOrScalar) -> PointType:
        """Divide `self` by `other` and return a new Point."""
        return self.__op(other, operator.floordiv)

    def __ifloordiv__(self, other: PointOrIterableOrScalar) -> PointType:
        """Divide `self` by `other` in-place and return `self`."""
        return self.__iop(other, operator.floordiv)

    def __pow__(self, exponent: float) -> PointType:
        """Raise each coordinate by `exponent` and return a new Point."""
        return Point(self.x ** exponent, self.y ** exponent)

    def __ipow__(self, exponent: float) -> PointType:
        """Raise each coordinate by `exponent` in-place and return self."""
        self.x **= exponent
        self.y **= exponent
        return self

    def __abs__(self) -> PointType:
        """Apply absolute value to each coordinate and return a new Point."""
        return Point(abs(self.x), abs(self.y))

    def __neg__(self) -> PointType:
        """Negate each coordinate and return a new Point."""
        return self * -1

    def __invert__(self) -> PointType:
        """Inverts each coordinate and return a new Point."""
        return Point(~self.x, ~self.y)

    def distance(self, other: PointOrIterable = None) -> float:
        """Return the floating point distance between `self` and `other`.

        If other is not given, the distance from self to the origin is
        returned.

        :param other: PointType
        :return: float
        """
        return (self.distance_squared(other or Point())) ** 0.5

    def distance_squared(self, other: PointOrIterable = None) -> float:
        """Return the floating point squared distance between self and other.

        If other is not given, the squared distance from self to the
        origin is returned.

        :param other: PointType
        :return: float
        """
        return sum((((other or Point()) - self) ** 2))

    def dot(self, other: PointOrIterable) -> float:
        """Return a scalar dot product of self with other.

        :param other: PointOrIterableOrScalar
        :return: float
        """
        return sum(self * other)

    def cross(self, other: PointOrIterable) -> float:
        """Return a scalar cross product of self with other.

        :param other: PointOrIterableOrScalar
        :return: float
        """
        try:
            return (self.x * other.y) + (self.y * other.x)
        except AttributeError:
            pass
        return (self.x * other[1]) + (self.y * other[0])

    def ccw(self, b: PointOrIterable, c: PointOrIterable) -> float:
        """Return a floating point value indicating the winding
        direction of the points [self, b, c].

        If ccw < 0,  clock-wise winding
        If ccw > 0,  counter clock-wise winding
        If ccw == 0, the three points are colinear

        Note: ccw is also 2*area of the triangle [self, b, c].

        :param b: Point
        :param c: Point
        :return: float
        """
        try:
            return ((b.x - self.x) * (c.y - self.y)) - ((c.x - self.x) * (b.y - self.y))
        except AttributeError:
            pass

        return ((b[0] - self.x) * (c[1] - self.y)) - ((c[0] - self.x) * (b[1] - self.y))

    def is_ccw(self, b: PointOrIterable, c: PointOrIterable) -> bool:
        """Return True if the angle [self, b, c] has counter clock-wise
        winding, else False.

        Raises the exception `ColinearPoints` if the points compose a line.

        :param b: Point
        :param c: Point
        :return: bool
        """
        result = self.ccw(b, c)
        if result == 0:
            raise ColinearPoints(self, b, c)
        return result > 0

    def is_colinear(self, b: PointType, c: PointType) -> bool:
        """True if the angle [self, b, c ] is a line, else False.

        :param b: Point
        :param c: Point
        :return: bool
        """
        return self.ccw(b, c) == 0

    def midpoint(self, other: PointType = None) -> PointType:
        """Return a new Point midway between `self` and `other`.

        If other is not given, the midpoint between self and the
        origin is returned.

        :param other: Point
        :return: Point
        """
        return (self + (other or Point())) / 2

    def between(self, p: PointType, q: PointType) -> bool:
        """True if self is bounded by the points [p, q], else False

        The bounds are checked by less than or equal to (<=) so self is
        considered between if it resides on any of the lines constructed
        using [p,q].

        :param p: Point
        :param q: Point
        :return: bool
        """

        i = min(p.x, q.x) <= self.x <= max(p.x, q.x)
        j = min(p.y, q.y) <= self.y <= max(p.y, q.y)

        return i and j

    def inside(self, p: PointType, q: PointType) -> bool:
        """True if self is bounded by the points (p, q), else False

        The bounds are checked by less than (<) so self is considered
        inside if it does not reside on any of the lines constructed
        using (p,q).

        :param p: Point
        :param q: Point
        :return: bool
        """

        # XXX re-implement with ccw and a list of points instead of a pair

        i = min(p.x, q.x) < self.x < max(p.x, q.x)
        j = min(p.y, q.y) < self.y < max(p.y, q.y)

        return i and j


# @dataclass(eq=True, order=True)
# class HashablePoint(Point):
#    pass
