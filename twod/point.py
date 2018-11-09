import math
from dataclasses import dataclass
from .exceptions import ColinearPoints


@dataclass
class Point:
    x: int = 0
    y: int = 0

    @property
    def is_origin(self):
        """
        """
        return self.x == 0 and self.y == 0

    def __iter__(self):
        """
        """
        return iter((self.x, self.y))

    def __add__(self, other):
        """
        """
        try:
            return Point(self.x + other.x, self.y + other.y)
        except AttributeError:
            pass
        return Point(self.x + other, self.y + other)

    def __iadd__(self, other):
        """
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

    def __sub__(self, other):
        """
        """
        try:
            return Point(self.x - other.x, self.y - other.y)
        except AttributeError:
            pass
        return Point(self.x - other, self.y - other)

    def __isub__(self, other):
        """
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

    def __mul__(self, other):
        """
        """
        try:
            return Point(self.x * other.x, self.y * other.y)
        except AttributeError:
            pass
        return Point(self.x * other, self.y * other)

    def __imul__(self, other):
        """
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

    def __truediv__(self, other):
        """
        """
        try:
            return Point(self.x / other.x, self.y / other.y)
        except AttributeError:
            pass
        return Point(self.x / other, self.y / other)

    def __itruediv__(self, other):
        """
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

    def __floordiv__(self, other):
        """
        """
        try:
            return Point(self.x // other.x, self.y // other.y)
        except AttributeError:
            pass
        return Point(self.x // other, self.y // other)

    def __ifloordiv__(self, other):
        """
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

    def __pow__(self, exponent):
        """
        """
        return Point(self.x ** exponent, self.y ** exponent)

    def __ipow__(self, exponent):
        """
        """
        self.x **= exponent
        self.y **= exponent
        return self

    def __abs__(self):
        """
        """
        return Point(abs(self.x), abs(self.y))

    def __neg__(self):
        """
        """
        return Point(-self.x, -self.y)

    def distance(self, other=None):
        """
        """
        return math.sqrt(self.distance_squared(other or Point()))

    def distance_squared(self, other=None):
        """
        """
        return sum((((other or Point()) - self) ** 2))

    def dot(self, other):
        """
        """
        return sum(self * other)

    def cross(self, other):
        """
        """
        return (self.x * other.y) + (self.y * other.x)

    def ccw(self, b, c):
        """
        """
        return ((b.x - self.x) * (c.y - self.y)) - ((c.x - self.x) * (b.y - self.y))

    def is_ccw(self, b, c):
        """
        """
        result = self.ccw(b, c)
        if result == 0:
            raise ColinearPoints(self, b, c)
        return result > 0

    def is_colinear(self, b, c):
        """
        """
        return self.ccw(b, c) == 0

    def midpoint(self, other=None):
        """
        """
        return (self + (other or Point())) / 2

    def between(self, p, q):
        """
        """
        i = (p.x <= self.x <= q.x) or (q.x <= self.x <= p.x)
        j = (p.y <= self.y <= q.y) or (p.y <= self.y <= p.y)
        return i and j
