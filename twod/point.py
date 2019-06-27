""" a two-dimensional point for humans™.
"""

import math
import sys
from dataclasses import astuple, dataclass
from typing import Iterable
from .types import Numeric, Coordinate, PointOrScalar, PointType
from .constants import EPSILON_EXP_MINUS_1, Quadrant
from .exceptions import ColinearPoints


@dataclass
class Point:
    x: float = 0
    y: float = 0
    """The Point class is a representation of a two dimensional
    geometric point with 'x' and 'y' attributes and many helpful
    properties and methods.

    >>> p = Point()
    >>> p.is_origin
    True
    """

    @classmethod
    def from_polar(cls, radius: float, theta: float, is_radians: bool = True):
        """Returns a Point with polar coordinates (R, ϴ).

        :param float radius:
        :param float theta:
        :param bool is_radians:
        :return: Point
        """
        theta = theta if is_radians else math.radians(theta)
        point = cls()
        point.polar = (radius, theta)
        return point

    @property
    def is_origin(self) -> bool:
        """Returns True if and only if x == 0 and y == 0.
        """
        return self.x == 0 and self.y == 0

    @property
    def quadrant(self) -> int:
        """The quadrant in the cartesian plane this point is located in:
        Quadrant.I, Quadrant.II, Quadrant.III, Quadrant.IV or Quadrant.ORIGIN.
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
        """Computes cartesian coordinates from polar coordinates expressed
        as a dimensionless radius and angle in radians.

        :param float radius:
        :param float radians:

        """
        self.x = round(radius * math.cos(radians), EPSILON_EXP_MINUS_1)
        self.y = round(radius * math.sin(radians), EPSILON_EXP_MINUS_1)

    @property
    def radius(self) -> float:
        """The distance from this point to the origin.
        """
        return math.hypot(self.x, self.y)

    @radius.setter
    def radius(self, new_value: float):
        self._polar_to_cartesian(new_value, self.radians)

    @property
    def radians(self) -> float:
        """The angle in radians measured counter-clockwise from 3 o'clock.
        """
        return math.atan2(self.y, self.x)

    @radians.setter
    def radians(self, new_value: float) -> None:
        self._polar_to_cartesian(self.radius, new_value)

    @property
    def degrees(self) -> float:
        """The angle in degrees measured counter-clockwise from 3 o'clock.
        """
        return math.degrees(self.radians)

    @degrees.setter
    def degrees(self, new_value: float) -> None:
        self._polar_to_cartesian(self.radius, math.radians(new_value))

    @property
    def polar(self) -> Coordinate:
        """Polar coordinates tuple: (R, ϴ).
        R is the distance from the origin to this point.
        ϴ is the angle measured counter-clockwise from 3 o'clock, expressed in radians.
        """
        return (self.radius, self.radians)

    @polar.setter
    def polar(self, new_values: Coordinate) -> None:
        try:
            radius, radians, *_ = map(float, new_values)
            self._polar_to_cartesian(radius, radians)
            return
        except (TypeError, ValueError):
            pass

        raise TypeError(f"Expected a numeric iterable, got {type(new_values)}")

    @property
    def polar_deg(self) -> Coordinate:
        """Polar coordinates tuple: (R, ϴ).
        R is the distance from the origin to this point.
        ϴ is the angle measured counter-clockwise from 3 o'clock, expressed in degrees.
        """
        radius, radians = self.polar
        return (radius, math.degrees(radians))

    @polar_deg.setter
    def polar_deg(self, new_values: Coordinate) -> None:
        try:
            radius, degrees, *_ = map(float, new_values)
            self._polar_to_cartesian(radius=radius, radians=math.radians(degrees))
            return
        except (TypeError, ValueError):
            pass
        raise TypeError(f"Expected a numeric iterable, got {type(new_values)}")

    @property
    def xy(self) -> Coordinate:
        """A tuple of this point's x and y coordinates.
        """
        return (self.x, self.y)

    @xy.setter
    def xy(self, new_values: Coordinate) -> None:
        try:
            self.x, self.y, *_ = map(float, new_values)
            return
        except (TypeError, ValueError):
            pass
        raise TypeError(f"Expected a numeric iterable, got {type(new_values)}")

    def __iter__(self) -> Iterable[Coordinate]:
        """Returns an iterator over tuple of the classes' fields; x and y.
        """
        return iter(astuple(self))

    def __add__(self, other: PointOrScalar) -> PointType:
        """Adds other to self and returns a new Point.

        If other has attributes x and y, returns a new
        Point:

        Point(self.x + other.x, self.y + other.y)

        Otherwise, other is treated as a scalar and added
        to both x and y:

        Point(self.x + other, self.y + other)

        """
        try:
            return Point(self.x + other.x, self.y + other.y)
        except AttributeError:
            pass
        return Point(self.x + other, self.y + other)

    def __iadd__(self, other: PointOrScalar) -> PointType:
        """Adds other to self in-place and returns self.

        If other has attributes x and y, adds those
        values to self in-place.

        Otherwise, other is treated as a scalar value and
        added to both x and y in-place.
        """
        try:
            self.x += other.x
            self.y += other.y
            return self
        except AttributeError:
            pass
        self.x += other
        self.y += other
        return self

    def __sub__(self, other: PointOrScalar) -> PointType:
        """Subtracts other from self and returns a new Point.

        If other has attributes x and y, returns a new
        Point:

        Point(self.x - other.x, self.y - other.y)

        Otherwise, other is treated as a scalar and subtracted
        from both x and y:

        Point(self.x - other, self.y - other)
        """
        try:
            return Point(self.x - other.x, self.y - other.y)
        except AttributeError:
            pass
        return Point(self.x - other, self.y - other)

    def __isub__(self, other: PointOrScalar) -> PointType:
        """Subtracts other from self in-place and returns self.

        If other has attributes x and y, subtracts those
        values from self in-place.

        Otherwise, other is treated as a scalar value and
        subtracted from both x and y in-place.
        """
        try:
            self.x -= other.x
            self.y -= other.y
            return self
        except AttributeError:
            pass
        self.x -= other
        self.y -= other
        return self

    def __mul__(self, other: PointOrScalar) -> PointType:
        """Multiplies other to self and returns a new Point.

        If other has attributes x and y, returns a new
        Point:

        Point(self.x * other.x, self.y * other.y)

        Otherwise, other is treated as a scalar and multiplied
        with both x and y:

        Point(self.x * other, self.y * other)
        """
        try:
            return Point(self.x * other.x, self.y * other.y)
        except AttributeError:
            pass
        return Point(self.x * other, self.y * other)

    def __imul__(self, other: PointOrScalar) -> PointType:
        """Multiplies other to self in-place and returns self.

        If other has attributes x and y, multiplies those
        values with self in-place.

        Otherwise, other is treated as a scalar value and
        multiplied with both x and y in-place.
        """
        try:
            self.x *= other.x
            self.y *= other.y
            return self
        except AttributeError:
            pass
        self.x *= other
        self.y *= other
        return self

    def __truediv__(self, other: PointOrScalar) -> PointType:
        """Divides self with other and returns a new Point.

        If other has attributes x and y, returns a new
        Point:

        Point(self.x / other.x, self.y / other.y)

        Otherwise, other is treated as a scalar and divides
        both x and y:

        Point(self.x / other, self.y / other)

        """
        try:
            return Point(self.x / other.x, self.y / other.y)
        except AttributeError:
            pass
        return Point(self.x / other, self.y / other)

    def __itruediv__(self, other: PointOrScalar) -> PointType:
        """Divides self with other in-place and returns self.

        If other has attributes x and y, self is divided by
        those values in-place.

        Otherwise, other is treated as a scalar value and
        divides both x and y in-place.
        """
        try:
            self.x /= other.x
            self.y /= other.y
            return self
        except AttributeError:
            pass
        self.x /= other
        self.y /= other
        return self

    def __floordiv__(self, other: PointOrScalar) -> PointType:
        """Divides self with other and returns a new Point.

        If other has attributes x and y, returns a new
        Point:

        Point(self.x // other.x, self.y // other.y)

        Otherwise, other is treated as a scalar and divides
        both x and y:

        Point(self.x // other, self.y // other)
        """
        try:
            return Point(self.x // other.x, self.y // other.y)
        except AttributeError:
            pass
        return Point(self.x // other, self.y // other)

    def __ifloordiv__(self, other: PointOrScalar) -> PointType:
        """Divides self with other in-place and returns self.

        If other has attributes x and y, self is divided by
        those values in-place.

        Otherwise, other is treated as a scalar value and
        divides both x and y in-place.
        """
        try:
            self.x //= other.x
            self.y //= other.y
            return self
        except AttributeError:
            pass
        self.x //= other
        self.y //= other
        return self

    def __pow__(self, exponent: float) -> PointType:
        """Raises each coordinate to the given exponent and
        returns a new Point.

        """
        return Point(self.x ** exponent, self.y ** exponent)

    def __ipow__(self, exponent: float) -> PointType:
        """Raises each coordinate to the given exponent
        in-place and returns self.
        """
        self.x **= exponent
        self.y **= exponent
        return self

    def __abs__(self) -> PointType:
        """Applies the absolute value function to each
        coordinate and returns a new Point.
        """
        return Point(abs(self.x), abs(self.y))

    def __neg__(self) -> PointType:
        """Applies negation to each coordinate and returns
        a new Point.
        """
        return self * -1

    def __invert__(self) -> PointType:
        """Inverts each coordinate and returns a new Point.
        """
        return Point(~self.x, ~self.y)

    def distance(self, other: PointType = None) -> float:
        """Returns the floating point distance between self and other.
        If other is not specified, the distance from self to the origin
        is calculated.
        """
        return (self.distance_squared(other or Point())) ** 0.5

    def distance_squared(self, other: PointType = None) -> float:
        """Returns the floating point squared distance between self and other.
        If other is not specified, the sequared distance from self to the
        origin is calculated.
        """
        return sum((((other or Point()) - self) ** 2))

    def dot(self, other: PointOrScalar) -> float:
        """Returns a scalar dot product of self with other.
        """
        return sum(self * other)

    def cross(self, other: PointOrScalar) -> float:
        """Returns a scalar cross product of self with other.
        """
        return (self.x * other.y) + (self.y * other.x)

    def ccw(self, b: PointType, c: PointType) -> float:
        """Returns a floating point value indicating the winding
        direction of the points [self, b, c].

        If ccw < 0,  clock-wise winding
        If ccw > 0,  counter clock-wise winding
        If ccw == 0, the three points are colinear

        Note: ccw is also 2*area of the triangle [self, b, c].

        """
        return ((b.x - self.x) * (c.y - self.y)) - ((c.x - self.x) * (b.y - self.y))

    def is_ccw(self, b: PointType, c: PointType) -> bool:
        """Returns True if the angle [self, b, c] has counter clock-wise
        winding, else False.

        Raises the exception ColinearPoints if the points are
        colinear.
        """
        result = self.ccw(b, c)
        if result == 0:
            raise ColinearPoints(self, b, c)
        return result > 0

    def is_colinear(self, b: PointType, c: PointType) -> bool:
        """Returns True if the angle [self, b, c ] is a line, else False.
        """
        return self.ccw(b, c) == 0

    def midpoint(self, other: PointType = None) -> PointType:
        """Returns a new Point between self and other. If other is not
        specified, the midpoint between self and the origin is calculated.
        """
        return (self + (other or Point())) / 2

    def between(self, p: PointType, q: PointType) -> bool:
        """Returns True if self is bounded by the points [p, q], else False

        The bounds are checked by less than or equal to (<=) so self is
        considered between if it resides on any of the lines constructed
        using [p,q].
        """

        i = min(p.x, q.x) <= self.x <= max(p.x, q.x)
        j = min(p.y, q.y) <= self.y <= max(p.y, q.y)

        return i and j

    def inside(self, p: PointType, q: PointType) -> bool:
        """Returns True if self is bounded by the points (p, q), else False

        The bounds are checked by less than (<) so self is considered
        inside if it does not reside on any of the lines constructed
        using (p,q).
        """

        i = min(p.x, q.x) < self.x < max(p.x, q.x)
        j = min(p.y, q.y) < self.y < max(p.y, q.y)

        return i and j


# @dataclass(eq=True, order=True)
# class HashablePoint(Point):
#    pass
