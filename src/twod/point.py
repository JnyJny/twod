"""a two-dimensional point for humans™."""

from __future__ import annotations

import math
import operator
from dataclasses import dataclass
from typing import Any, Callable, Iterable, Optional, Self

from .constants import EPSILON_EXP_MINUS_1, Quadrant
from .exceptions import ColinearPoints


@dataclass(slots=True)
class Point:
    """A two dimensional geometric point.

    The Point class represents a geometric point with 'x' and 'y' attributes
    and has many helpful properties and methods.

    Points are mutable, so they are not hashable and cannot be put in a set
    or used as a dictionary key. Use the xy property when you need a
    hashable value.

    >>> p = Point()
    >>> p.is_origin
    True
    """

    x: float = 0.0
    y: float = 0.0

    @classmethod
    def from_polar(
        cls,
        radius: float,
        theta: float,
        is_radians: bool = True,
        translate: Optional[Point] = None,
    ) -> Self:
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

    @classmethod
    def from_any(
        cls,
        value: Any,
        scalar_ok: bool = True,
        is_polar: bool = False,
    ) -> Self:
        """Returns a Point made from a variety of inputs.

        Accepted values:
        - Point: returned as is
        - complex: real is x, imaginary is y
        - dict: keys "x" and "y"
        - list or tuple: (x, y), or (radius, radians) if is_polar is True
        - int or float: used for both x and y if scalar_ok is True
        - str: parsed as a complex number, e.g. "1+2j"

        Raises TypeError if value cannot be converted.

        :param value: Any
        :param bool scalar_ok: accept a lone number as (value, value)
        :param bool is_polar: interpret a list or tuple as (radius, radians)
        :return: Point
        """
        match value:
            case Point():
                return value
            case complex():
                return cls(value.real, value.imag)
            case dict():
                return cls(value["x"], value["y"])
            case list() | tuple():
                if is_polar:
                    return cls.from_polar(value[0], value[1])
                return cls(value[0], value[1])
            case float() | int():
                if scalar_ok:
                    return cls(value, value)
            case str():
                try:
                    z = complex(value)
                except ValueError:
                    pass
                else:
                    return cls(z.real, z.imag)

        raise TypeError(f"unable to convert {value!r} to {cls.__name__}")

    @staticmethod
    def _coerce(value: Any) -> Point:
        """Returns value as a Point without accepting a lone number."""
        return Point.from_any(value, scalar_ok=False)

    @property
    def is_origin(self) -> bool:
        """True if and only if x == 0 and y == 0."""
        return self.x == 0 and self.y == 0

    @property
    def quadrant(self) -> Quadrant:
        """The quadrant in the cartesian plane this point is located in.

        Possible values are:
        - Quadrant.FIRST
        - Quadrant.SECOND
        - Quadrant.THIRD
        - Quadrant.FOURTH
        - Quadrant.ORIGIN
        - Quadrant.X_AXIS
        - Quadrant.Y_AXIS
        """

        if self.is_origin:
            return Quadrant.ORIGIN

        if self.x == 0 and self.y != 0:
            return Quadrant.Y_AXIS

        if self.y == 0 and self.x != 0:
            return Quadrant.X_AXIS

        if self.x > 0:
            return Quadrant.FIRST if self.y > 0 else Quadrant.FOURTH
        else:
            return Quadrant.SECOND if self.y > 0 else Quadrant.THIRD

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
    def polar(self) -> tuple[float, float]:
        """Polar coordinates tuple: (R, ϴ).

        R is the distance from the origin to this point.
        ϴ is the angle (radians) measured counter-clockwise from 3 o'clock.
        """
        return (self.radius, self.radians)

    @polar.setter
    def polar(self, new_values: Iterable[int | float]) -> None:
        try:
            radius, radians, *_ = map(float, new_values)
            self._polar_to_cartesian(radius, radians)
            return
        except (TypeError, ValueError):
            raise TypeError(
                f"Expected a Iterable[int |float], got {new_values!r}"
            ) from None

    @property
    def polar_deg(self) -> tuple[float, float]:
        """Polar coordinates tuple: (R, ϴ).

        R is the distance from the origin to this point.
        ϴ is the angle (degrees) measured counter-clockwise from 3 o'clock.
        """
        radius, radians = self.polar
        return (radius, math.degrees(radians))

    @polar_deg.setter
    def polar_deg(self, new_values: Iterable[int | float]) -> None:
        try:
            radius, degrees, *_ = map(float, new_values)
            self._polar_to_cartesian(radius=radius, radians=math.radians(degrees))
            return
        except (TypeError, ValueError):
            raise TypeError(
                f"Expected a Iterable[int|float], got {new_values!r}"
            ) from None

    @property
    def xy(self) -> tuple[float, float]:
        """A tuple of this point's x and y coordinates."""
        return (self.x, self.y)

    @xy.setter
    def xy(self, new_values: Iterable[int | float]) -> None:
        try:
            self.x, self.y, *_ = map(float, new_values)
            return
        except (TypeError, ValueError):
            raise TypeError(
                f"Expected a Iterable[int | float], got {new_values!r}"
            ) from None

    def __iter__(self) -> Iterable[float]:
        """An iterator over x and y coordinates."""
        return iter(self.xy)

    def __len__(self) -> int:
        return 2

    def __eq__(self, other: object) -> bool:

        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y

        if isinstance(other, (tuple, list)):
            return self.x == other[0] and self.y == other[1]

        return NotImplemented

    def __getitem__(self, key: int | slice) -> float | tuple[float, ...]:

        if isinstance(key, int):
            if key == 0:
                return self.x
            if key == 1:
                return self.y
            raise IndexError(f"Key out of range: {key}")

        if isinstance(key, slice):
            return self.xy[key]

        raise TypeError(f"Expected int or slice key, not {key!r}")

    def __setitem__(self, key: int, value: int | float) -> None:
        if not isinstance(key, int):
            raise TypeError(f"Expected int key, not {key!r}")
        if key == 0:
            self.x = value
            return
        if key == 1:
            self.y = value
            return
        raise IndexError(f"Key out of range: {key}")

    def _op(self, other: Any, op: Callable) -> Point:
        """Applies op to each component of Point and other."""

        if isinstance(other, Point):
            return Point(op(self.x, other.x), op(self.y, other.y))

        if isinstance(other, (list, tuple)):
            return Point(op(self[0], other[0]), op(self[1], other[1]))

        if isinstance(other, (float, int)):
            return Point(op(self.x, other), op(self.y, other))

        return NotImplemented

    def _iop(self, other: Any, op: Callable) -> Self:
        """Updates the current Point by applying op to each component
        of other."""

        if isinstance(other, Point):
            self.x = op(self.x, other.x)
            self.y = op(self.y, other.y)
            return self

        if isinstance(other, (list, tuple)):
            self.x = op(self.x, other[0])
            self.y = op(self.y, other[1])
            return self

        if isinstance(other, (float, int)):
            self.x = op(self.x, other)
            self.y = op(self.y, other)
            return self

        return NotImplemented

    def __add__(self, other: Point | Iterable[int | float] | int | float) -> Point:
        return self._op(other, operator.add)

    def __iadd__(self, other: Point | Iterable[int | float] | int | float) -> Self:
        return self._iop(other, operator.add)

    def __sub__(self, other: Point | Iterable[int | float] | int | float) -> Point:
        return self._op(other, operator.sub)

    def __isub__(self, other: Point | Iterable[int | float] | int | float) -> Self:
        return self._iop(other, operator.sub)

    def __mul__(self, other: Point | Iterable[int | float] | int | float) -> Point:
        return self._op(other, operator.mul)

    def __imul__(self, other: Point | Iterable[int | float] | int | float) -> Self:
        try:
            return self._iop(other, operator.mul)
        except ZeroDivisionError:
            raise ZeroDivisionError(repr(other)) from None

    def __truediv__(self, other: Point | Iterable[int | float] | int | float) -> Point:
        try:
            return self._op(other, operator.truediv)
        except ZeroDivisionError:
            raise ZeroDivisionError(repr(other)) from None

    def __itruediv__(self, other: Point | Iterable[int | float] | int | float) -> Self:
        try:
            return self._iop(other, operator.truediv)
        except ZeroDivisionError:
            raise ZeroDivisionError(repr(other)) from None

    def __floordiv__(self, other: Point | Iterable[int | float] | int | float) -> Point:
        try:
            return self._op(other, operator.floordiv)
        except ZeroDivisionError:
            raise ZeroDivisionError(repr(other)) from None

    def __ifloordiv__(self, other: Point | Iterable[int | float] | int | float) -> Self:
        return self._iop(other, operator.floordiv)

    def __pow__(self, exponent: float) -> Point:
        return Point(self.x**exponent, self.y**exponent)

    def __ipow__(self, exponent: float) -> Self:
        self.x **= exponent
        self.y **= exponent
        return self

    def __abs__(self) -> Point:
        return Point(abs(self.x), abs(self.y))

    def __neg__(self) -> Point:
        return self * -1

    def distance(self, other: PointLike | None = None) -> float:
        """Return the floating point distance between self and other.

        If other is not given, the distance from self to the origin is
        returned.

        :param other: Point or (x, y) sequence
        :return: float
        """
        other = Point() if other is None else self._coerce(other)
        return math.hypot(other.x - self.x, other.y - self.y)

    def distance_squared(self, other: PointLike | None = None) -> float:
        """Return the squared distance between self and other.

        If other is not given, the squared distance from self to the
        origin is returned.

        :param other: Point or (x, y) sequence
        :return: float
        """
        other = Point() if other is None else self._coerce(other)
        dx, dy = other.x - self.x, other.y - self.y
        return dx * dx + dy * dy

    def dot(self, other: PointLike) -> float:
        """Return a scalar dot product of self with other.

        :param other: Point or (x, y) sequence
        :return: float
        """
        other = self._coerce(other)
        return self.x * other.x + self.y * other.y

    def cross(self, other: PointLike) -> float:
        """Return a scalar cross product of self with other.

        :param other: Point or (x, y) sequence
        :return: float
        """
        other = self._coerce(other)
        return (self.x * other.y) - (self.y * other.x)

    def ccw(self, b: PointLike, c: PointLike) -> float:
        """Return a floating point value indicating the winding
        direction of the points [self, b, c].

        If ccw < 0,  clock-wise winding
        If ccw > 0,  counter clock-wise winding
        If ccw == 0, the three points are colinear

        Note: ccw is also 2*area of the triangle [self, b, c].

        :param b: Point or (x, y) sequence
        :param c: Point or (x, y) sequence
        :return: float
        """
        b, c = self._coerce(b), self._coerce(c)
        return ((b.x - self.x) * (c.y - self.y)) - ((c.x - self.x) * (b.y - self.y))

    def is_ccw(self, b: PointLike, c: PointLike) -> bool:
        """Return True if the angle [self, b, c] has counter clock-wise
        winding, else False.

        Raises the exception ColinearPoints if the points compose a line.

        :param b: Point or (x, y) sequence
        :param c: Point or (x, y) sequence
        :return: bool
        """
        result = self.ccw(b, c)
        if result == 0:
            raise ColinearPoints(self, b, c)
        return result > 0

    def is_colinear(self, b: PointLike, c: PointLike) -> bool:
        """True if the angle [self, b, c ] is a line, else False.

        :param b: Point or (x, y) sequence
        :param c: Point or (x, y) sequence
        :return: bool
        """
        return self.ccw(b, c) == 0

    def midpoint(self, other: PointLike | None = None) -> Point:
        """Return a new Point midway between self and other..

        If other is not given, the midpoint between self and the
        origin is returned.

        :param other: Point or (x, y) sequence
        :return: Point
        """
        other = Point() if other is None else self._coerce(other)
        return Point((self.x + other.x) / 2, (self.y + other.y) / 2)

    def between(self, p: PointLike, q: PointLike) -> bool:
        """True if self is bounded by the points [p, q], else False

        The bounds are checked by less than or equal to (<=) so self is
        considered between if it resides on any of the lines constructed
        using [p,q].

        :param p: Point or (x, y) sequence
        :param q: Point or (x, y) sequence
        :return: bool
        """
        p, q = self._coerce(p), self._coerce(q)

        i = min(p.x, q.x) <= self.x <= max(p.x, q.x)
        j = min(p.y, q.y) <= self.y <= max(p.y, q.y)

        return i and j

    def inside(self, p: PointLike, q: PointLike) -> bool:
        """True if point is bounded by the points (p, q), else False

        The bounds are checked by less than (<) so point is considered
        inside if it does not reside on any of the lines constructed
        using (p,q).

        :param p: Point or (x, y) sequence
        :param q: Point or (x, y) sequence
        :return: bool
        """

        # XXX re-implement with ccw and a list of points instead of a pair

        p, q = self._coerce(p), self._coerce(q)

        i = min(p.x, q.x) < self.x < max(p.x, q.x)
        j = min(p.y, q.y) < self.y < max(p.y, q.y)

        return i and j

    def rotate(
        self,
        theta: float,
        origin: PointLike | None = None,
        is_degrees: bool = False,
        inplace: bool = True,
    ) -> Point:
        """Rotate this point counter-clockwise by theta about origin.

        If origin is not given, the point is rotated about (0, 0).

        :param float theta: angle, in radians unless is_degrees is True
        :param origin: Point or (x, y) sequence
        :param bool is_degrees: theta is in degrees
        :param bool inplace: update this point and return it, otherwise
            return a new Point
        :return: Point
        """
        if is_degrees:
            theta = math.radians(theta)

        origin = Point() if origin is None else self._coerce(origin)

        cos, sin = math.cos(theta), math.sin(theta)
        dx, dy = self.x - origin.x, self.y - origin.y
        x = origin.x + dx * cos - dy * sin
        y = origin.y + dx * sin + dy * cos

        if inplace:
            self.x, self.y = x, y
            return self

        return Point(x, y)

    def scale(self, factor: float) -> Self:
        """Multiply both coordinates by factor, in place, and return self.

        :param float factor:
        :return: Point
        """
        self.x *= factor
        self.y *= factor
        return self


PointLike = Point | tuple[float, float] | list[float]
"""Anything the geometry methods accept in place of a Point."""
