"""
"""

from .point import Point

from dataclasses import dataclass


@dataclass
class Rect(Point):
    w: int = 0
    h: int = 0

    def __iter__(self):
        return iter((self.x, self.y, self.w, self.h))

    @property
    def A(self):
        return Point(self.x, self.y)

    @property
    def B(self):
        return Point(self.x + self.w, self.y)

    @property
    def C(self):
        return Point(self.x, self.y) + Point(self.w, self.h)

    @property
    def D(self):
        return Point(self.x, self.y + self.h)

    @property
    def vertices(self):
        return [self.A, self.B, self.C, self.D]

    @property
    def center(self):
        return self.A.midpoint(self.C)

    def __contains__(self, other):

        if not isinstance(other, Rect):
            return other.between(self.A, self.C)

        for v in other.vertices:
            if v.between(self.A, self.C):
                return True

        for v in self.vertices:
            if v.between(other.A, other.C):
                return True

        return False

    def __add__(self, other):
        return Rect(
            self.x + other.x,
            self.y + other.y,
            self.w + other.w,
            self.h + other.h,
        )

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.w += other.w
        self.h += other.h
        return self

    def __sub__(self, other):

        return Rect(
            self.x - other.x,
            self.y - other.y,
            self.w - other.w,
            self.h - other.h,
        )

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.w -= other.w
        self.h -= other.h
        return self

    def __mul__(self, other):
        return Rect(
            self.x * other.x,
            self.y * other.y,
            self.w * other.w,
            self.h * other.h,
        )

    def __imul__(self, other):
        self.x *= other.x
        self.y *= other.y
        self.w *= other.w
        self.h *= other.h
        return self

    def __truediv__(self, other):
        try:
            return Rect(
                self.x / other.x,
                self.y / other.y,
                self.w / other.w,
                self.h / other.h,
            )
        except ZeroDivisionError:
            raise ZeroDivisionError(value)

    def __itruediv__(self, other):
        try:
            self.x /= other.x
            self.y /= other.y
            self.w /= other.w
            self.h /= other.h
            return self
        except ZeroDivisionError:
            raise ZeroDivisonError(value)

    def __floordiv__(self, other):
        try:
            return Rect(
                self.x // other.x,
                self.y // other.y,
                self.w // other.w,
                self.h // other.h,
            )
        except ZeroDivisionError:
            raise ZeroDivisionError(value)

    def __ifloordiv__(self, value):
        try:
            self.x //= other.x
            self.y //= other.y
            self.w //= other.w
            self.h //= other.h
            return self
        except ZeroDivisionError:
            raise ZeroDivisionError(value)
