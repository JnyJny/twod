"""an ellipse for humans™"""

from __future__ import annotations

from .centered import Centered
from .point import Point, PointLike


class Ellipse(Centered):
    """An ellipse centered at (x, y) with its major axis along the x-axis.

    major_axis and minor_axis are the semi-axes: the distances from the
    center to the vertices and co-vertices.
    """

    def __init__(
        self,
        x: float = 0.0,
        y: float = 0.0,
        minor_axis: float = 0,
        major_axis: float = 0,
    ) -> None:
        self._p = Point(x, y)
        self.minor_axis = minor_axis
        self.major_axis = major_axis

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(x={self.x}, y={self.y}, "
            f"minor_axis={self.minor_axis}, major_axis={self.major_axis})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Ellipse):
            return NotImplemented
        return (
            self.xy == other.xy
            and self.minor_axis == other.minor_axis
            and self.major_axis == other.major_axis
        )

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
    def is_circle(self) -> bool:
        """Returns True if this ellipse is also a circle."""
        return self.minor_axis == self.major_axis

    def __contains__(self, other: PointLike) -> bool:
        """True if other is strictly inside this ellipse.

        Points on the ellipse itself are not contained. An ellipse with a
        zero-length axis contains nothing.

        Raises TypeError if other cannot be converted to a Point.
        """
        other = Point.from_any(other, scalar_ok=False)
        dx, dy = other.x - self.x, other.y - self.y
        a, b = self.major_axis, self.minor_axis
        return (dx * b) ** 2 + (dy * a) ** 2 < (a * b) ** 2


class Circle(Centered):
    """A circle centered at (x, y)."""

    def __init__(self, x: float = 0.0, y: float = 0.0, radius: float = 0) -> None:
        self._p = Point(x, y)
        self.radius = radius

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(x={self.x}, y={self.y}, radius={self.radius})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Circle):
            return NotImplemented
        return self.xy == other.xy and self.radius == other.radius

    def __contains__(self, other: PointLike) -> bool:
        """True if other is strictly inside this circle.

        Points on the circle itself are not contained. A circle without a
        positive radius contains nothing.

        Raises TypeError if other cannot be converted to a Point.
        """
        other = Point.from_any(other, scalar_ok=False)
        dx, dy = other.x - self.x, other.y - self.y
        return self.radius > 0 and dx * dx + dy * dy < self.radius**2
