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
                return any(v in self for v in other.vertices)

        return NotImplemented

    @property
    def A(self) -> Point:
        return self._p

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

        A, B, C, D = self.vertices
        return [
            A.distance(B),
            B.distance(C),
            C.distance(D),
            D.distance(A),
        ]

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
        return self._op(other, operator.truediv)

    def __ifloordiv__(self, other: CRect | Point) -> CRect:
        return self._op(other, operator.truediv, inplace=True)
