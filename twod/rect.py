"""a two dimensional Rectangle 
"""

from .point import Point

from dataclasses import dataclass, astuple


@dataclass
class Rect(Point):
    w: int = 0
    h: int = 0

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
        """
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
        self.x *= other.x
        self.y *= other.y
        try:
            self.w *= other.w
            self.h *= other.h
        except AttributeError:
            pass
        return self

    def __truediv__(self, other):
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
            raise ZeroDivisionError(other)

    def __itruediv__(self, other):
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
            raise ZeroDivisionError(other)

    def __floordiv__(self, other):
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
            raise ZeroDivisionError(other)

    def __ifloordiv__(self, other):
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
            raise ZeroDivisionError(other)
