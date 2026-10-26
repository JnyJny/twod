"""a rectangle for humans™"""

from __future__ import annotations

import operator
from typing import Callable, Self

from .point import Point, PointLike


class Rect:
    """A rectangle specified by an origin at (x,y) and
    dimensions (w,h).
    """

    def __init__(
        self,
        x: float | int = 0,
        y: float | int = 0,
        w: float | int = 0,
        h: float | int = 0,
    ) -> None:
        self._p = Point(x, y)
        self._d = Point(w, h)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(x={self.x}, y={self.y}, w={self.w}, h={self.h})"
        )

    @property
    def x(self) -> float:
        return self._p.x

    @x.setter
    def x(self, new_x: float) -> None:
        self._p.x = new_x

    @property
    def y(self) -> float:
        return self._p.y

    @y.setter
    def y(self, new_y: float) -> None:
        self._p.y = new_y

    @property
    def xy(self) -> tuple[float, float]:
        return self._p.xy

    @xy.setter
    def xy(self, xy: tuple[float, float]) -> None:
        self._p.xy = xy

    @property
    def w(self) -> float:
        return self._d.x

    @w.setter
    def w(self, new_width: float | int) -> None:
        self._d.x = new_width

    @property
    def h(self) -> float:
        return self._d.y

    @h.setter
    def h(self, new_height: float | int) -> None:
        self._d.y = new_height

    @property
    def wh(self) -> tuple[float, float]:
        return self._d.xy

    @wh.setter
    def wh(self, new_wh: tuple[float | int, float | int]) -> None:
        self._d.xy = new_wh

    @property
    def A(self) -> Point:
        """Point at (x,y)."""
        return Point(self.x, self.y)

    @property
    def B(self) -> Point:
        """Point at (x+w, y)."""
        return self._p + (self.w, 0)

    @property
    def C(self) -> Point:
        """Point at (x+w, y+h)."""
        return self._p + self.wh

    @property
    def D(self) -> Point:
        """Point at (x, y+h)."""
        return self._p + (0, self.h)

    @property
    def vertices(self) -> list[Point]:
        """The points A, B, C, and D in a list."""
        return [self.A, self.B, self.C, self.D]

    @property
    def sides(self) -> list[float]:
        """The lengths of each side: AB, BC, CD, and DA."""
        w, h = abs(self.w), abs(self.h)
        return [w, h, w, h]

    @property
    def center(self) -> Point:
        """Point at the center of the rectangle (midpoint of AC)."""
        return self.A.midpoint(self.C)

    @center.setter
    def center(self, new_center) -> None:
        self._p.xy = (Point(*new_center) - (Point(self.w, self.h) / 2)).xy

    @property
    def perimeter(self) -> float:
        """The distance around this rectangle."""
        return sum(self.sides)

    @property
    def area(self) -> float:
        """The area of this rectangle."""
        return self.w * self.h

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rect):
            return NotImplemented
        return self._p == other._p and self._d == other._d

    def __contains__(self, other: Rect | PointLike) -> bool:
        """If other is a twod.Point, returns True if the point is inside this
        rectangle.

        If other is a twod.Rect, returns True if all of other's vertices are
        inside this rectangle. Rectangles that share an edge or are the same
        rectangle are not contained; use intersects to test for overlap.

        Raises TypeError if other is not a Point or Rect.
        """

        if isinstance(other, (tuple, list)):
            other = Point.from_any(other)

        if not isinstance(other, (Rect, Point)):
            raise TypeError(f"expected Point or Rect, got {other!r}")

        left, top, right, bottom = self._extent

        if isinstance(other, Point):
            return left < other.x < right and top < other.y < bottom

        other_left, other_top, other_right, other_bottom = other._extent
        return (
            left < other_left
            and other_right < right
            and top < other_top
            and other_bottom < bottom
        )

    @property
    def _extent(self) -> tuple[float, float, float, float]:
        """The (min x, min y, max x, max y) of this rectangle."""
        x, y = self._p.x, self._p.y
        x2, y2 = x + self._d.x, y + self._d.y
        return min(x, x2), min(y, y2), max(x, x2), max(y, y2)

    def intersects(self, other: Rect) -> bool:
        """True if this rectangle and other share any area.

        Rectangles that only touch along an edge or at a corner do not
        intersect.

        Raises TypeError if other is not a Rect.
        """
        if not isinstance(other, Rect):
            raise TypeError(f"expected Rect, got {other!r}")

        left, top, right, bottom = self._extent
        other_left, other_top, other_right, other_bottom = other._extent
        return (
            left < other_right
            and other_left < right
            and top < other_bottom
            and other_top < bottom
        )

    @staticmethod
    def _operand(other: object) -> Point | Rect | None:
        """Returns other as a Point or Rect, or None if it is neither."""
        if isinstance(other, (tuple, list)):
            return Point.from_any(other)
        if isinstance(other, (Point, Rect)):
            return other
        return None

    def _op(self, other: Rect | PointLike, op: Callable) -> Rect:
        operand = self._operand(other)
        if operand is None:
            return NotImplemented
        other = operand
        x = op(self.x, other.x)
        y = op(self.y, other.y)
        if isinstance(other, Rect):
            w = op(self.w, other.w)
            h = op(self.h, other.h)
        else:
            w = self.w
            h = self.h
        return Rect(x, y, w, h)

    def _iop(self, other: Rect | PointLike, op: Callable) -> Self:
        operand = self._operand(other)
        if operand is None:
            return NotImplemented
        other = operand
        self.x = op(self.x, other.x)
        self.y = op(self.y, other.y)
        if isinstance(other, Rect):
            self.w = op(self.w, other.w)
            self.h = op(self.h, other.h)
        return self

    def __add__(self, other: Rect | PointLike) -> Rect:
        return self._op(other, operator.add)

    def __iadd__(self, other: Rect | PointLike) -> Self:
        return self._iop(other, operator.add)

    def __sub__(self, other: Rect | PointLike) -> Rect:
        return self._op(other, operator.sub)

    def __isub__(self, other: Rect | PointLike) -> Self:
        return self._iop(other, operator.sub)

    def __mul__(self, other: Rect | PointLike) -> Rect:
        return self._op(other, operator.mul)

    def __imul__(self, other: Rect | PointLike) -> Self:
        return self._iop(other, operator.mul)

    def __truediv__(self, other: Rect | PointLike) -> Rect:
        try:
            return self._op(other, operator.truediv)
        except ZeroDivisionError:
            raise ZeroDivisionError(repr(other)) from None

    def __itruediv__(self, other: Rect | PointLike) -> Self:
        try:
            return self._iop(other, operator.truediv)
        except ZeroDivisionError:
            raise ZeroDivisionError(repr(other)) from None

    def __floordiv__(self, other: Rect | PointLike) -> Rect:
        try:
            return self._op(other, operator.floordiv)
        except ZeroDivisionError:
            raise ZeroDivisionError(repr(other)) from None

    def __ifloordiv__(self, other: Rect | PointLike) -> Self:
        try:
            return self._iop(other, operator.floordiv)
        except ZeroDivisionError:
            raise ZeroDivisionError(repr(other)) from None
