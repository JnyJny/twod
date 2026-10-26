"""a position mixin for shapes located by their center, for humans™"""

from __future__ import annotations

from ..point import Point, PointLike


class Centered:
    """Gives a shape x, y, xy and center properties backed by a Point.

    The class using this mixin assigns the center Point to self._p, the same
    way Rect does, and is otherwise free to be anything. The shape is not a
    Point and has none of Point's arithmetic or polar coordinate methods.

    >>> class Disc(Centered):
    ...     def __init__(self, x, y):
    ...         self._p = Point(x, y)
    >>> disc = Disc(1, 2)
    >>> disc.xy
    (1, 2)
    >>> disc.center = (3, 4)
    >>> disc.x
    3.0
    """

    _p: Point

    @property
    def x(self) -> float:
        """The x coordinate of the center."""
        return self._p.x

    @x.setter
    def x(self, new_x: float) -> None:
        self._p.x = new_x

    @property
    def y(self) -> float:
        """The y coordinate of the center."""
        return self._p.y

    @y.setter
    def y(self, new_y: float) -> None:
        self._p.y = new_y

    @property
    def xy(self) -> tuple[float, float]:
        """A tuple of the center's x and y coordinates."""
        return self._p.xy

    @xy.setter
    def xy(self, new_xy: PointLike) -> None:
        self._p.xy = Point.from_point_like(new_xy).xy

    @property
    def center(self) -> Point:
        """A copy of the center Point; assign to move the shape."""
        return Point(self._p.x, self._p.y)

    @center.setter
    def center(self, new_center: PointLike) -> None:
        self.xy = new_center
