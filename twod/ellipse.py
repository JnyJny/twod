""" an ellipse for humans™
"""

from dataclasses import dataclass
from math import pi, tau

from .point import Point


@dataclass
class Ellipse(Point):
    minor_axis: int = 0
    major_axis: int = 0

    @property
    def e(self):
        """The eccentricity of this ellipse expressed as a float.
        """
        return (1 + (self.minor_axis ** 2 / self.major_axis ** 2)) ** 0.5

    @property
    def focus1(self):
        """The first focus of the ellipse.
        """
        return Point(self.e, self.y)

    @property
    def focus2(self):
        """The second focus of the ellipse.
        """
        return Point(-self.e, self.y)

    @property
    def vertices(self):
        """A list of Points that are major_axis distance
        from the center of the ellipse on the x-axis.
        """

        p = Point(self.x + self.major_axis, self.y)
        q = Point(-(self.x + self.major_axis), self.y)
        return [p, q]

    @property
    def co_vertices(self):
        """A list of Points that are minor_axis distance
        from the center of the ellipse on the y-axis.
        """
        p = Point(self.x, self.y + self.minor_axis)
        q = Point(self.x, -(self.y + self.minor_axis))
        return [p, q]

    @property
    def is_circle(self):
        """Returns True if this ellipse is also a circle.
        """
        return self.minor_axis == self.major_axis

    def __contains__(self, other):
        pass


@dataclass
class Circle(Point):
    radius: int = 0

    def __contains__(self, other):
        pass
