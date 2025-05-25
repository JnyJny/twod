""" """

from __future__ import annotations

import cmath
import math
import operator
from typing import Any, Callable

from .constants import Quadrant
from .exceptions import ColinearPoints


class CPoint:
    __slots__ = ("_z",)

    @classmethod
    def from_any(
        cls,
        value: Any,
        scalar_ok: bool = True,
        is_polar: bool = False,
    ) -> CPoint:
        match value:
            case cls():
                return value
            case complex():
                return cls(value.real, value.imag)
            case dict():
                return cls(value["x"], value["y"])
            case list() | tuple():
                if is_polar:
                    return cls.from_polar(value[0], value[1])
                else:
                    return cls(value[0], value[1])
            case float() | int():
                if scalar_ok:
                    return cls(value, value)
            case str():
                try:
                    z = complex(value)
                    return cls(z.real, z.imag)
                except ValueError:
                    pass

        raise TypeError(f"unable to convert {value!r} to {cls}")

    @classmethod
    def from_complex(cls, z: complex) -> CPoint:
        print("z", z)
        return cls(z.real, z.imag)

    @classmethod
    def from_polar(
        cls,
        radius: float,
        theta: float,
        is_radians: bool = True,
        translate: Any = None,
    ) -> CPoint:

        if not is_radians:
            theta = math.radians(theta)

        r = cmath.rect(radius, theta)

        print(f"{radius=} {theta=} {r=}")

        p = cls.from_complex(cmath.rect(radius, theta))

        if translate is not None:
            p += cls.from_any(translate)
        return p

    def __init__(self, x: float | int = 0, y: float | int = 0) -> None:
        self._z = complex(x, y)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"

    @property
    def x(self) -> float:
        return self._z.real

    @x.setter
    def x(self, new_x: float | int) -> None:
        self._z = complex(new_x, self._z.imag)

    @property
    def y(self) -> float:
        return self._z.imag

    @y.setter
    def y(self, new_y: float | int) -> None:
        self._z = complex(self._z.real, new_y)

    @property
    def xy(self) -> tuple[float, float]:
        return (self._z.real, self._z.imag)

    @xy.setter
    def xy(self, new_xy: Any) -> None:
        self._z = self.__class__.from_any(new_xy, scalar_ok=False)._z

    @property
    def radius(self) -> float:
        return abs(self._z)

    @radius.setter
    def radius(self, new_radius: float | int) -> None:
        self._z = cmath.rect(new_radius, self.radians)

    @property
    def radians(self) -> float:
        return cmath.phase(self._z)

    @radians.setter
    def radians(self, new_radians: float | int) -> None:
        self._z = cmath.rect(self.radius, new_radians)

    @property
    def degrees(self) -> float:
        return math.degrees(self.radians)

    @degrees.setter
    def degrees(self, new_degrees: float | int) -> None:
        self.radians = math.radians(new_degrees)

    @property
    def polar(self) -> tuple[float, float]:
        return cmath.polar(self._z)

    @property
    def is_origin(self) -> bool:
        return not bool(self._z)

    @property
    def quadrant(self) -> Quadrant:

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

    def __len__(self) -> int:
        return 2

    def __getitem__(self, key: int | slice) -> float:
        match key:
            case int():
                return self.xy[key]
            case slice():
                return self.xy[key][0]
        raise TypeError(f"Unknown key {key} expected int or slice")

    def __setitem__(self, key: int, value: float | int) -> None:

        if key == 0:
            self.x = value
            return
        if key == 1:
            self.y = value
            return

        raise IndexError(f"Key out of range: {key}")

    def __eq__(self, other: Any) -> bool:
        other = self.__class__.from_any(other)
        return cmath.isclose(self._z, other._z)

    def _op(self, other: Any, op: Callable, inplace: bool = False) -> CPoint:
        try:
            other = self.__class__.from_any(other)
            x, y = op(self.x, other.x), op(self.y, other.y)
            result = complex(x, y)
            if inplace:
                self._z = result
                return self
            return self.__class__(result.real, result.imag)
        except (TypeError, IndexError, KeyError):
            return NotImplemented

    def __add__(self, other: Any) -> CPoint:
        return self._op(other, operator.add)

    def __iadd__(self, other: Any) -> CPoint:
        return self._op(other, operator.add, inplace=True)

    def __sub__(self, other: Any) -> CPoint:
        return self._op(other, operator.sub)

    def __isub__(self, other: Any) -> CPoint:
        return self._op(other, operator.sub, inplace=True)

    def __mul__(self, other: Any) -> CPoint:
        return self._op(other, operator.mul)

    def __imul__(self, other: Any) -> CPoint:
        return self._op(other, operator.mul, inplace=True)

    def __truediv__(self, other: Any) -> CPoint:
        other = self.__class__.from_any(other)
        return self.__class__(self.x / other.x, self.y / other.y)

    def __itruediv__(self, other: Any) -> CPoint:
        other = self.__class__.from_any(other)
        self._z = complex(self.x / other.x, self.y / other.y)
        return self

    # EJO unimplemented magic methods
    #     - floordiv, ifloordiv: nonsensical with complex numbers
    #     - pow, ipow: no obvious geometric application
    #     - bitwise ops: also nonsensical

    def distance(self, other: Any = None) -> float:
        other = self.__class__.from_any(other)
        return abs(self._z - other._z)

    def _cmul(self, other: Any = None) -> complex:
        """Multiply self._z.conjugate() by other"""
        other = self.__class__.from_any(other)
        return self._z.conjugate() * other._z

    def dot(self, other: Any = None) -> float:
        return self._cmul(other).real

    def cross(self, other: Any = None) -> float:
        return self._cmul(other).imag

    def ccw(self, b: Any, c: Any) -> float:
        """Returns a float indicating the winding direction of
        the points [self, b, c].

        If result > 0, clock-wise winding.
        If result < 0, counter clock-wise winding (ccw).
        If result = 0, the three points are colinear.

        Note: ccw is also 2*area of the triangle [self, b, c]
        """
        b = self.__class__.from_any(b)
        c = self.__class__.from_any(c)

        return (b - self).cross(c - self)

    def is_ccw(self, b: Any, c: Any) -> bool:

        result = self.ccw(b, c)
        if result == 0:
            raise ColinearPoints(self, b, c)
        return result > 0

    def is_colinear(self, b: Any, c: Any) -> bool:
        return self.ccw(b, c) == 0

    def midpoint(self, other: Any = None) -> CPoint:
        other = self.__class__.from_any(other)
        print(other, self + other, (self + other) / 2)
        return (self + other) / 2

    def _bounds(self, p: Any, q: Any, op: Callable) -> bool:

        p = self.__class__.from_any(p)
        q = self.__class__.from_any(q)

        min_x, max_x = sorted((p.x, q.x))
        min_y, max_y = sorted((p.y, q.y))
        return all(
            [
                op(min_x, self.x) and op(self.x, max_x),
                op(min_y, self.y) and op(self.y, max_y),
            ]
        )

    def between(self, p: Any, q: Any) -> bool:
        return self._bounds(p, q, operator.le)

    def inside(self, p: Any, q: Any) -> bool:
        return self._bounds(p, q, operator.lt)

    def rotate(
        self,
        theta: float | int,
        origin: Any = None,
        is_degrees: bool = False,
        inplace: bool = True,
    ) -> CPoint:

        if is_degrees:
            theta = math.radians(theta)

        origin = self.__class__.from_any(origin)

        rotator = complex(math.cos(theta), math.sin(theta))

        result = origin._z + (self._z - origin._z) * rotator

        if inplace:
            self._z = result
            return self

        return self.__class__.from_complex(result)

    def scale(self, scale: float | int) -> CPoint:
        self._z *= cmath.rect(scale, 0)
        return self
