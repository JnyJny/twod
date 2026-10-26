"""an ellipse for humans™"""

from dataclasses import dataclass

from .point import Point


@dataclass
class Ellipse(Point):
    """An ellipse centered at (x, y) with its major axis along the x-axis.

    major_axis and minor_axis are the semi-axes: the distances from the
    center to the vertices and co-vertices.
    """

    minor_axis: int = 0
    major_axis: int = 0

    @property
    def e(self) -> float:
        """The eccentricity of this ellipse expressed as a float."""
        return (1 - (self.minor_axis**2 / self.major_axis**2)) ** 0.5

    @property
    def focal_distance(self) -> float:
        """The distance from the center to each focus."""
        return self.major_axis * self.e

    @property
    def focus1(self) -> Point:
        """The focus to the right of the center."""
        return Point(self.x + self.focal_distance, self.y)

    @property
    def focus2(self) -> Point:
        """The focus to the left of the center."""
        return Point(self.x - self.focal_distance, self.y)

    @property
    def vertices(self) -> list[Point]:
        """A list of Points that are major_axis distance from the center
        of the ellipse on the x-axis: right, then left.
        """
        return [
            Point(self.x + self.major_axis, self.y),
            Point(self.x - self.major_axis, self.y),
        ]

    @property
    def co_vertices(self) -> list[Point]:
        """A list of Points that are minor_axis distance from the center
        of the ellipse on the y-axis: above, then below.
        """
        return [
            Point(self.x, self.y + self.minor_axis),
            Point(self.x, self.y - self.minor_axis),
        ]

    @property
    def is_circle(self):
        """Returns True if this ellipse is also a circle."""
        return self.minor_axis == self.major_axis

    def __contains__(self, other):
        pass


@dataclass
class Circle(Point):
    radius: float = 0

    def __contains__(self, other):
        pass
