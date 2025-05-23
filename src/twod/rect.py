"""a rectangle for humans™"""

from __future__ import annotations

import operator
from typing import Callable

from .point import Point


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
        return self._p

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
        # EJO this needs work, why the max? The abs might be
        #     needed either since direction is clockwise?

        A, B, C, D = self.vertices
        return [
            max(abs(A - B).xy),
            max(abs(B - C).xy),
            max(abs(C - D).xy),
            max(abs(D - A).xy),
        ]

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

    def __contains__(self, other: Point | Rect) -> bool:
        """If other is a twod.Point, returns True if the point is inside this
        rectangle.

        If other is a twod.Rect, returns True if any of other's vertices are
        inside this rectangle.

        Otherwise returns False.

        Raises TypeError if other is not a Point or Rect.
        """

        if not isinstance(other, (Rect, Point)):
            raise TypeError("expected Point or Rect, got {other!r}")

        if isinstance(other, Point):
            return other.inside(self.A, self.C) and other.inside(self.B, self.D)

        return any(v in self for v in other.vertices)

    def _op(self, other: Point | Rect, op: Callable) -> Rect:
        x = op(self.x, other.x)
        y = op(self.y, other.y)
        if isinstance(other, Rect):
            w = op(self.w, other.w)
            h = op(self.h, other.h)
        else:
            w = self.w
            h = self.h
        return Rect(x, y, w, h)

    def _iop(self, other: Point | Rect, op: Callable) -> Rect:
        self.x = op(self.x, other.x)
        self.y = op(self.y, other.y)
        if isinstance(other, Rect):
            self.w = op(self.w, other.w)
            self.h = op(self.h, other.h)
        return self

    def __add__(self, other: Point | Rect) -> Rect:
        return self._op(other, operator.add)

    def __iadd__(self, other: Point | Rect) -> Rect:
        return self._iop(other, operator.add)

    def __sub__(self, other: Point | Rect) -> Rect:
        return self._op(other, operator.sub)

    def __isub__(self, other: Point | Rect) -> Rect:
        return self._iop(other, operator.sub)

    def __mul__(self, other: Point | Rect) -> Rect:
        return self._op(other, operator.mul)

    def __imul__(self, other: Point | Rect) -> Rect:
        return self._iop(other, operator.mul)

    def __truediv__(self, other: Point | Rect) -> Rect:
        try:
            return self._op(other, operator.truediv)
        except ZeroDivisionError:
            raise ZeroDivisionError(repr(other)) from None

    def __itruediv__(self, other: Point | Rect) -> Rect:
        try:
            return self._iop(other, operator.truediv)
        except ZeroDivisionError:
            raise ZeroDivisionError(repr(other)) from None

    def __floordiv__(self, other: Point | Rect) -> Rect:
        try:
            return self._op(other, operator.floordiv)
        except ZeroDivisionError:
            raise ZeroDivisionError(repr(other)) from None

    def __ifloordiv__(self, other: Point | Rect) -> Rect:
        try:
            return self._iop(other, operator.floordiv)
        except ZeroDivisionError:
            raise ZeroDivisionError(repr(other)) from None
