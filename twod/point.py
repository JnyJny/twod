""" a two-dimensional geometric point.
"""

import math
from dataclasses import dataclass, astuple
from .exceptions import ColinearPoints


@dataclass
class Point:
    x: int = 0
    y: int = 0
    """The Point class is a representation of a two dimensional
    geometric point. It has an 'x' coordinate and a 'y' coordinate.


    >>> p = Point()
    >>> p.is_origin
    True
    """

    @property
    def is_origin(self):
        """Returns True iff x == 0 and y == 0.
        """
        return self.x == 0 and self.y == 0

    def __iter__(self):
        """Returns a interator over x and y.
        """
        return iter(astuple(self))

    def __add__(self, other):
        """Adds other to self and returns a new Point.

        If other has attributes x and y, returns a new
        Point:

        Point(self.x + other.x, self.y + other.y)

        Otherwise, other is treated as a scalar and added
        to both x and y:

        Point(self.x + other, self.y + other)

        """
        try:
            return Point(self.x + other.x, self.y + other.y)
        except AttributeError:
            pass
        return Point(self.x + other, self.y + other)

    def __iadd__(self, other):
        """Adds other to self in-place and returns self.
        
        If other has attributes x and y, adds those
        values to self in-place.
        
        Otherwise, other is treated as a scalar value and
        added to both x and y in-place.
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
        """Subtracts other from self and returns a new Point.

        If other has attributes x and y, returns a new
        Point:

        Point(self.x - other.x, self.y - other.y)

        Otherwise, other is treated as a scalar and subtracted
        from both x and y:

        Point(self.x - other, self.y - other)
        """
        try:
            return Point(self.x - other.x, self.y - other.y)
        except AttributeError:
            pass
        return Point(self.x - other, self.y - other)

    def __isub__(self, other):
        """Subtracts other from self in-place and returns self.
        
        If other has attributes x and y, subtracts those
        values from self in-place.
        
        Otherwise, other is treated as a scalar value and
        subtracted from both x and y in-place.
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
        """Multiplies other to self and returns a new Point.

        If other has attributes x and y, returns a new
        Point:

        Point(self.x * other.x, self.y * other.y)

        Otherwise, other is treated as a scalar and multiplied
        with both x and y:

        Point(self.x * other, self.y * other)
        """
        try:
            return Point(self.x * other.x, self.y * other.y)
        except AttributeError:
            pass
        return Point(self.x * other, self.y * other)

    def __imul__(self, other):
        """Multiplies other to self in-place and returns self.
        
        If other has attributes x and y, multiplies those
        values with self in-place.
        
        Otherwise, other is treated as a scalar value and
        multiplied with both x and y in-place.
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
        """Divides self with other and returns a new Point.

        If other has attributes x and y, returns a new
        Point:

        Point(self.x / other.x, self.y / other.y)

        Otherwise, other is treated as a scalar and divides
        both x and y:

        Point(self.x / other, self.y / other)

        """
        try:
            return Point(self.x / other.x, self.y / other.y)
        except AttributeError:
            pass
        return Point(self.x / other, self.y / other)

    def __itruediv__(self, other):
        """Divides self with other in-place and returns self.
        
        If other has attributes x and y, self is divided by
        those values in-place.
        
        Otherwise, other is treated as a scalar value and
        divides both x and y in-place.
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
        """Divides self with other and returns a new Point.

        If other has attributes x and y, returns a new
        Point:

        Point(self.x // other.x, self.y // other.y)

        Otherwise, other is treated as a scalar and divides
        both x and y:

        Point(self.x // other, self.y // other)
        """
        try:
            return Point(self.x // other.x, self.y // other.y)
        except AttributeError:
            pass
        return Point(self.x // other, self.y // other)

    def __ifloordiv__(self, other):
        """Divides self with other in-place and returns self.
        
        If other has attributes x and y, self is divided by
        those values in-place.
        
        Otherwise, other is treated as a scalar value and
        divides both x and y in-place.
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
        """Raises each coordinate to the given exponent and
        returns a new Point.
        
        """
        return Point(self.x ** exponent, self.y ** exponent)

    def __ipow__(self, exponent):
        """Raises each coordinate to the given exponent
        in-place and returns self.
        """
        self.x **= exponent
        self.y **= exponent
        return self

    def __abs__(self):
        """Applies the absolute value function to each
        coordinate and returns a new Point.
        """
        return Point(abs(self.x), abs(self.y))

    def __neg__(self):
        """Applies negation to each coordinate and returns
        a new Point.
        """
        return self * -1

    def __invert__(self):
        """Inverts each coordinate of self and returns a new Point.
        """
        return Point(~self.x, ~self.y)

    def distance(self, other=None):
        """Returns the floating point distance between self and other.
        If other is not specified, the distance from self to the origin
        is calculated.

        Note: This method is implemented with math.sqrt and may incur
              a performance penalty making it not suitable for tight loops.
              For partial ordering, see the distance_squared method.

        """
        return math.sqrt(self.distance_squared(other or Point()))

    def distance_squared(self, other=None):
        """Returns the floating point squared distance between self and other.
        If other is not specified, the sequared distance from self to the
        origin is calculated.
        
        Note: 
        
        """
        return sum((((other or Point()) - self) ** 2))

    def dot(self, other):
        """Returns a scalar dot product of self with other.
        """
        return sum(self * other)

    def cross(self, other):
        """Returns a scalar cross product of self with other.
        """
        return (self.x * other.y) + (self.y * other.x)

    def ccw(self, b, c):
        """Returns a floating point value indicating the winding
        direction of the points [self, b, c]. 

        If ccw < 0,  clock-wise winding
        If ccw > 0,  counter clock-wise winding
        If ccw == 0, the three points are colinear
        
        Note: ccw is also 2*area of the triangle [self, b, c].
        
        """
        return ((b.x - self.x) * (c.y - self.y)) - (
            (c.x - self.x) * (b.y - self.y)
        )

    def is_ccw(self, b, c):
        """Returns True if the angle [self, b, c] has counter clock-wise
        winding, else False.

        Raises the exception ColinearPoints if the points are
        colinear.
        """
        result = self.ccw(b, c)
        if result == 0:
            raise ColinearPoints(self, b, c)
        return result > 0

    def is_colinear(self, b, c):
        """Returns True if the angle [self, b, c ] is a line, else False.
        """
        return self.ccw(b, c) == 0

    def midpoint(self, other=None):
        """Returns a new Point between self and other. If other is not
        specified, the midpoint between self and the origin is calculated.
        """
        return (self + (other or Point())) / 2

    def between(self, p, q):
        """Returns True if self is bounded by the points [p, q], else False
        
        The bounds are checked by less than or equal to (<=) so self is
        considered between if it resides on any of the lines constructed
        using [p,q]. 
        """

        i = self.x >= min(p.x, q.x) and self.x <= max(p.x, q.x)
        j = self.y >= min(p.y, q.y) and self.y <= max(p.y, q.y)

        return i and j

    def inside(self, p, q):
        """Returns True if self is bounded by the points (p, q), else False

        The bounds are checked by less than (<) so self is considered
        inside if it does not reside on any of the lines constructed
        using (p,q).
        """

        i = self.x > min(p.x, q.x) and self.x < max(p.x, q.x)
        j = self.y > min(p.y, q.y) and self.y < max(p.y, q.y)

        return i and j


@dataclass(unsafe_hash=True)
class HashablePoint(Point):
    pass
