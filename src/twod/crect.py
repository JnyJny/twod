""" """

from __future__ import annotations

import operator
from typing import Any

from . import CPoint as Point
from .mixins import MixinDimension, MixinPoint


class CRect(MixinPoint, MixinDimension):
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
        name = self.__class__.__name__
        return f"{name}(x={self.x}, y={self.y}, w={self.w}, h={self.h})"

    def __eq__(self, other: CRect) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._p == other._p and self._d == other._d

    def __contains__(self, other: CRect | Point) -> bool:

        match other:
            case Point():
                return other.inside(*self.AC) and other.inside(*self.BD)
            case CRect():
                return all(v in self for v in other.vertices)

        raise TypeError(f"expected CPoint or CRect, got {other!r}")

    @property
    def _extent(self) -> tuple[float, float, float, float]:
        """The (min x, min y, max x, max y) of this rectangle."""
        x2, y2 = self.x + self.w, self.y + self.h
        return min(self.x, x2), min(self.y, y2), max(self.x, x2), max(self.y, y2)

    def intersects(self, other: CRect) -> bool:
        """True if this rectangle and other share any area.

        Rectangles that only touch along an edge or at a corner do not
        intersect.

        Raises TypeError if other is not a CRect.
        """
        if not isinstance(other, CRect):
            raise TypeError(f"expected CRect, got {other!r}")

        left, top, right, bottom = self._extent
        other_left, other_top, other_right, other_bottom = other._extent
        return (
            left < other_right
            and other_left < right
            and top < other_bottom
            and other_top < bottom
        )

    @property
    def A(self) -> Point:
        return Point(self.x, self.y)

    @property
    def B(self) -> Point:
        return self._p + Point(self.w, 0)

    @property
    def C(self) -> Point:
        return self._p + self._d

    @property
    def D(self) -> Point:
        return self._p + Point(0, self.h)

    @property
    def AB(self) -> tuple[Point, Point]:
        return (self.A, self.B)

    @property
    def BC(self) -> tuple[Point, Point]:
        return (self.B, self.C)

    @property
    def CD(self) -> tuple[Point, Point]:
        return (self.C, self.D)

    @property
    def DA(self) -> tuple[Point, Point]:
        return (self.D, self.A)

    @property
    def AC(self) -> tuple[Point, Point]:
        return (self.A, self.C)

    @property
    def BD(self) -> tuple[Point, Point]:
        return (self.B, self.D)

    @property
    def vertices(self) -> list[Point]:
        return [self.A, self.B, self.C, self.D]

    @property
    def sides(self) -> list[float]:

        w, h = abs(self.w), abs(self.h)
        return [w, h, w, h]

    @property
    def perimeter(self) -> float:
        return sum(self.sides)

    @property
    def area(self) -> float:
        return self.w * self.h

    @property
    def center(self) -> Point:
        return self.A.midpoint(self.C)

    @center.setter
    def center(self, new_center: Any) -> None:
        p = self._p.__class__.from_any(new_center)
        self._p.xy = (p - (self._d / 2)).xy

    def _op(
        self,
        other: CRect | Point,
        op: operator,
        inplace: bool = False,
    ) -> CRect:

        match other:
            case CRect():
                p = op(self._p, other._p)
                d = op(self._d, other._d)
            case Point():
                p = op(self._p, other)
                d = self._d
            case _:
                return NotImplemented

        if inplace:
            self._p = p
            self._d = d
            return self
        return self.__class__(p.x, p.y, d.x, d.y)

    def __add__(self, other: CRect | Point) -> CRect:
        return self._op(other, operator.add)

    def __iadd__(self, other: CRect | Point) -> CRect:
        return self._op(other, operator.add, inplace=True)

    def __sub__(self, other: CRect | Point) -> CRect:
        return self._op(other, operator.sub)

    def __isub__(self, other: CRect | Point) -> CRect:
        return self._op(other, operator.sub, inplace=True)

    def __mul__(self, other: CRect | Point) -> CRect:
        return self._op(other, operator.mul)

    def __imul__(self, other: CRect | Point) -> CRect:
        return self._op(other, operator.mul, inplace=True)

    def __truediv__(self, other: CRect | Point) -> CRect:
        return self._op(other, operator.truediv)

    def __itruediv__(self, other: CRect | Point) -> CRect:
        return self._op(other, operator.truediv, inplace=True)

    def __floordiv__(self, other: CRect | Point) -> CRect:
        return self._op(other, operator.floordiv)

    def __ifloordiv__(self, other: CRect | Point) -> CRect:
        return self._op(other, operator.floordiv, inplace=True)
