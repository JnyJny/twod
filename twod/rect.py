"""a rectangle for humans™
"""

from dataclasses import astuple, dataclass

from .point import Point

from typing import Any
from typing import Dict
from typing import List


@dataclass
class Rect(Point):
    """A rectangle specified by an origin at (x,y) and
    dimensions (w,h).
    """

    w: int = 0
    h: int = 0

    @property
    def A(self) -> Point:
        """Point at (x,y)."""
        return Point(self.x, self.y)

    @property
    def B(self) -> Point:
        """Point at (x+w, y)."""
        return Point(self.x + self.w, self.y)

    @property
    def C(self) -> Point:
        """Point at (x+w, y+h)."""
        return Point(self.x + self.w, self.y + self.h)

    @property
    def D(self) -> Point:
        """Point at (x, y+h)."""
        return Point(self.x, self.y + self.h)

    @property
    def vertices(self) -> List[Point]:
        """The points A, B, C, and D in a list.
        """
        return [self.A, self.B, self.C, self.D]

    @property
    def sides(self) -> List[float]:
        """The lengths of each side: AB, BC, CD, and DA.
        """
        return [
            max(abs(self.A - self.B)),
            max(abs(self.B - self.C)),
            max(abs(self.C - self.D)),
            max(abs(self.D - self.A)),
        ]

    @property
    def center(self) -> Point:
        """Point at the center of the rectangle (midpoint of AC).
        """
        return self.A.midpoint(self.C)

    @center.setter
    def center(self, new_center):
        self.x, self.y = Point(*new_center) - (Point(self.w, self.h) / 2)

    @property
    def perimeter(self) -> float:
        """The distance around this rectangle.
        """
        return sum(self.sides)

    @property
    def area(self) -> float:
        """The area of this rectangle.
        """
        return self.w * self.h

    def __contains__(self, other) -> bool:
        """If other is a twod.Point, returns True if the point is inside this
        rectangle.

        If other is a twod.Rect, returns True if any of other's vertices are
        inside or any of the target rectangle's verices are inside other.

        Otherwise returns False.

        Raises TypeError if other is not a Point or Rect.

        """
        if not isinstance(other, Rect):
            try:
                return other.between(self.A, self.C)
            except AttributeError:
                pass
            raise TypeError(f"expected Point or Rect, received {type(other)}")

        for v in other.vertices:
            if v.between(self.A, self.C):
                return True

        for v in self.vertices:
            if v.between(other.A, other.C):
                return True

        return False

    def __add__(self, other):
        """
        :param Point|Rect other:
        :return: Rect
        """
        x = self.x + other.x
        y = self.y + other.y
        try:
            w = self.w + other.w
            h = self.h + other.h
        except AttributeError:
            w = self.w
            h = self.h
        return Rect(x, y, w, h)

    def __iadd__(self, other):
        """
        :param Point|Rect other:
        :return: Rect
        """
        self.x += other.x
        self.y += other.y
        try:
            self.w += other.w
            self.h += other.h
        except AttributeError:
            pass
        return self

    def __sub__(self, other):
        """
        :param Point|Rect other:
        :return: Rect
        """
        x = self.x - other.x
        y = self.y - other.y
        try:
            w = self.w - other.w
            h = self.h - other.h
        except AttributeError:
            w = self.w
            h = self.h
        return Rect(x, y, w, h)

    def __isub__(self, other):
        """
        :param Point|Rect other:
        :return: Rect
        """
        self.x -= other.x
        self.y -= other.y
        try:
            self.w -= other.w
            self.h -= other.h
        except AttributeError:
            pass
        return self

    def __mul__(self, other):
        """
        :param Point|Rect other:
        :return: Rect
        """
        x = self.x * other.x
        y = self.y * other.y
        try:
            w = self.w * other.w
            h = self.h * other.h
        except AttributeError:
            w = self.w
            h = self.h
        return Rect(x, y, w, h)

    def __imul__(self, other):
        """
        :param Point|Rect other:
        :return: Rect
        """
        self.x *= other.x
        self.y *= other.y
        try:
            self.w *= other.w
            self.h *= other.h
        except AttributeError:
            pass
        return self

    def __truediv__(self, other):
        """
        :param Point|Rect other:
        :return: Rect
        """
        try:
            x = self.x / other.x
            y = self.y / other.y
            try:
                w = self.w / other.w
                h = self.h / other.h
            except AttributeError:
                w = self.w
                h = self.h
            return Rect(x, y, w, h)
        except ZeroDivisionError:
            pass
        raise ZeroDivisionError(other)

    def __itruediv__(self, other):
        """
        :param Point|Rect other:
        :return: Rect
        """
        try:
            self.x /= other.x
            self.y /= other.y
            try:
                self.w /= other.w
                self.h /= other.h
            except AttributeError:
                pass
            return self
        except ZeroDivisionError:
            pass
        raise ZeroDivisionError(other)

    def __floordiv__(self, other):
        """
        :param Point|Rect other:
        :return: Rect
        """
        try:
            x = self.x // other.x
            y = self.y // other.y
            try:
                w = self.w // other.w
                h = self.h // other.h
            except AttributeError:
                w = self.w
                h = self.h
            return Rect(x, y, w, h)
        except ZeroDivisionError:
            pass
        raise ZeroDivisionError(other)

    def __ifloordiv__(self, other):
        """
        :param Point|Rect other:
        :return: Rect
        """
        try:
            self.x //= other.x
            self.y //= other.y
            try:
                self.w //= other.w
                self.h //= other.h
            except AttributeError:
                pass
            return self
        except ZeroDivisionError:
            pass
        raise ZeroDivisionError(other)
