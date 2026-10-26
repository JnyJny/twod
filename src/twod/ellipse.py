"""an ellipse for humans™"""

from dataclasses import dataclass

from .point import Point, PointLike


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
        """The eccentricity of this ellipse expressed as a float.

        Raises ValueError if minor_axis is longer than major_axis.
        """
        ratio = self.minor_axis**2 / self.major_axis**2
        if ratio > 1:
            raise ValueError(
                f"minor_axis {self.minor_axis} is longer than "
                f"major_axis {self.major_axis}"
            )
        return (1 - ratio) ** 0.5

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

    def __contains__(self, other: PointLike) -> bool:
        """True if other is strictly inside this ellipse.

        Points on the ellipse itself are not contained. An ellipse with a
        zero-length axis contains nothing.

        Raises TypeError if other cannot be converted to a Point.
        """
        other = self._coerce(other)
        dx, dy = other.x - self.x, other.y - self.y
        a, b = self.major_axis, self.minor_axis
        return (dx * b) ** 2 + (dy * a) ** 2 < (a * b) ** 2


@dataclass
class Circle(Point):
    """A circle centered at (x, y).

    Unlike Point.radius, which is the distance from the origin, radius here
    is the radius of the circle.
    """

    radius: float = 0

    def __contains__(self, other: PointLike) -> bool:
        """True if other is strictly inside this circle.

        Points on the circle itself are not contained.

        Raises TypeError if other cannot be converted to a Point.
        """
        return self.distance_squared(other) < self.radius**2 and self.radius > 0
