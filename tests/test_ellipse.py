"""Tests for ellipse.py module"""

import math

import pytest
from twod import Ellipse as ExportedEllipse
from twod import Point
from twod.ellipse import Circle, Ellipse


class TestEllipse:
    """Test cases for Ellipse class"""

    def test_ellipse_exported_from_package(self):
        """Ellipse is importable from the top level package"""
        assert ExportedEllipse is Ellipse

    def test_ellipse_creation(self):
        """Test basic ellipse creation"""
        e = Ellipse(x=0, y=0, minor_axis=3, major_axis=5)
        assert e.x == 0
        assert e.y == 0
        assert e.minor_axis == 3
        assert e.major_axis == 5

    def test_ellipse_default_values(self):
        """Test ellipse with default values"""
        e = Ellipse()
        assert e.x == 0.0
        assert e.y == 0.0
        assert e.minor_axis == 0
        assert e.major_axis == 0

    def test_ellipse_is_not_a_point(self):
        """An ellipse is not a point and has none of its methods"""
        e = Ellipse(x=2, y=3, minor_axis=4, major_axis=6)
        assert not isinstance(e, Point)
        assert not hasattr(e, "polar")
        assert not hasattr(e, "dot")

    def test_ellipse_center_is_a_copy(self):
        """Changing the center Point does not move the ellipse"""
        e = Ellipse(x=2, y=3, minor_axis=4, major_axis=6)
        assert e.center == Point(2, 3)
        e.center.x = 99
        assert e.x == 2

    def test_ellipse_position_properties(self):
        """x, y, xy and center read and write the center"""
        e = Ellipse(x=2, y=3, minor_axis=4, major_axis=6)
        assert e.xy == (2, 3)
        e.x = 5
        e.y = 6
        assert e.xy == (5, 6)
        e.xy = (7, 8)
        assert e.center == Point(7, 8)
        e.center = (9, 10)
        assert (e.x, e.y) == (9, 10)

    def test_ellipse_equality_and_repr(self):
        """Ellipses compare by center and axes"""
        a = Ellipse(1, 2, 3, 4)
        assert a == Ellipse(1, 2, 3, 4)
        assert a != Ellipse(1, 2, 3, 5)
        assert a != Circle(1, 2, 3)
        assert a != "ellipse"
        assert repr(a) == "Ellipse(x=1, y=2, minor_axis=3, major_axis=4)"

    def test_ellipse_is_unhashable(self):
        """Ellipses are mutable and so are not hashable"""
        with pytest.raises(TypeError):
            hash(Ellipse())

    def test_eccentricity_calculation(self):
        """Test eccentricity calculation"""
        # Standard ellipse (major > minor)
        e = Ellipse(minor_axis=3, major_axis=5)
        expected_e = math.sqrt(1 - (3**2 / 5**2))
        assert abs(e.e - expected_e) < 1e-10

    def test_eccentricity_circle(self):
        """Test eccentricity for circle (minor == major)"""
        e = Ellipse(minor_axis=5, major_axis=5)
        assert e.e == 0.0

    def test_eccentricity_zero_major_axis(self):
        """Test eccentricity with zero major axis"""
        e = Ellipse(minor_axis=3, major_axis=0)
        with pytest.raises(ZeroDivisionError):
            _ = e.e

    def test_focus_points(self):
        """Test focus point calculations"""
        e = Ellipse(x=2, y=3, minor_axis=3, major_axis=5)
        expected_e = math.sqrt(1 - (3**2 / 5**2))

        focus_distance = 5 * expected_e

        focus1 = e.focus1
        focus2 = e.focus2

        assert focus1 == Point(2 + focus_distance, 3)
        assert focus2 == Point(2 - focus_distance, 3)

    def test_focus_points_sum_of_distances_is_major_axis_length(self):
        """Every point on an ellipse is 2 * major_axis from the foci combined"""
        e = Ellipse(x=2, y=3, minor_axis=3, major_axis=5)
        vertex = e.vertices[0]
        total = vertex.distance(e.focus1) + vertex.distance(e.focus2)
        assert math.isclose(total, 2 * e.major_axis)

    def test_focus_points_of_circle_are_the_center(self):
        """A circle's foci coincide with its center"""
        e = Ellipse(x=2, y=3, minor_axis=5, major_axis=5)
        assert e.focus1 == Point(2, 3)
        assert e.focus2 == Point(2, 3)

    def test_vertices(self):
        """Test vertices calculation"""
        e = Ellipse(x=2, y=3, minor_axis=3, major_axis=5)
        vertices = e.vertices

        assert len(vertices) == 2
        assert vertices[0] == Point(2 + 5, 3)  # (7, 3)
        assert vertices[1] == Point(2 - 5, 3)  # (-3, 3)

    def test_co_vertices(self):
        """Test co-vertices calculation"""
        e = Ellipse(x=2, y=3, minor_axis=3, major_axis=5)
        co_vertices = e.co_vertices

        assert len(co_vertices) == 2
        assert co_vertices[0] == Point(2, 3 + 3)  # (2, 6)
        assert co_vertices[1] == Point(2, 3 - 3)  # (2, 0)

    def test_is_circle_true(self):
        """Test is_circle property when axes are equal"""
        e = Ellipse(minor_axis=5, major_axis=5)
        assert e.is_circle is True

    def test_is_circle_false(self):
        """Test is_circle property when axes are different"""
        e = Ellipse(minor_axis=3, major_axis=5)
        assert e.is_circle is False

    def test_is_circle_zero_axes(self):
        """Test is_circle with zero axes"""
        e = Ellipse(minor_axis=0, major_axis=0)
        assert e.is_circle is True

    @pytest.mark.parametrize(
        "point, expected",
        [
            [(0, 0), True],
            [(4.9, 0), True],
            [(5, 0), False],
            [(5.1, 0), False],
            [(0, 2.9), True],
            [(0, 3), False],
            [(0, -3), False],
            [(3, 2), True],
            [(4, 2), False],
            [(3, 1), True],
            [(-3, -1), True],
        ],
    )
    def test_contains_point(self, point, expected):
        """Points are strictly inside the ellipse boundary"""
        e = Ellipse(minor_axis=3, major_axis=5)
        assert (point in e) is expected
        assert (Point(*point) in e) is expected

    def test_contains_uses_center(self):
        """Containment is relative to the ellipse center"""
        e = Ellipse(x=10, y=20, minor_axis=3, major_axis=5)
        assert (10, 20) in e
        assert (0, 0) not in e
        assert (14, 20) in e

    def test_contains_zero_axis_contains_nothing(self):
        """A degenerate ellipse contains no points"""
        assert (0, 0) not in Ellipse()
        assert (0, 0) not in Ellipse(minor_axis=0, major_axis=5)

    def test_contains_rejects_other_types(self):
        """Unconvertible operands raise TypeError"""
        with pytest.raises(TypeError):
            "foo" in Ellipse(minor_axis=3, major_axis=5)

    def test_negative_axes(self):
        """Test ellipse with negative axes"""
        e = Ellipse(minor_axis=-3, major_axis=5)
        # Should work mathematically but may produce unusual results
        assert e.minor_axis == -3
        assert e.major_axis == 5

    def test_major_smaller_than_minor(self):
        """Test case where major axis is smaller than minor axis"""
        e = Ellipse(minor_axis=5, major_axis=3)
        # This is mathematically unusual but should not crash
        assert e.minor_axis == 5
        assert e.major_axis == 3


class TestCircle:
    """Test cases for Circle class"""

    def test_circle_creation(self):
        """Test basic circle creation"""
        c = Circle(x=1, y=2, radius=5)
        assert c.x == 1
        assert c.y == 2
        assert c.radius == 5

    def test_circle_default_values(self):
        """Test circle with default values"""
        c = Circle()
        assert c.x == 0.0
        assert c.y == 0.0
        assert c.radius == 0

    def test_circle_is_not_a_point(self):
        """A circle is not a point, so its radius is only the circle's radius"""
        c = Circle(x=3, y=4, radius=2)
        assert not isinstance(c, Point)
        assert not hasattr(c, "polar")
        assert c.radius == 2

    def test_circle_position_properties(self):
        """x, y, xy and center read and write the center"""
        c = Circle(x=3, y=4, radius=2)
        assert c.xy == (3, 4)
        c.xy = (5, 6)
        assert c.center == Point(5, 6)
        c.center = (7, 8)
        assert (c.x, c.y) == (7, 8)
        c.center.x = 99
        assert c.x == 7

    def test_circle_equality_and_repr(self):
        """Circles compare by center and radius"""
        c = Circle(1, 2, 3)
        assert c == Circle(1, 2, 3)
        assert c != Circle(1, 2, 4)
        assert c != Circle(2, 2, 3)
        assert repr(c) == "Circle(x=1, y=2, radius=3)"

    @pytest.mark.parametrize(
        "point, expected",
        [
            [(0, 0), True],
            [(3, 3), True],
            [(3, 4), False],
            [(5, 0), False],
            [(-4.9, 0), True],
            [(4, 4), False],
        ],
    )
    def test_circle_contains_point(self, point, expected):
        """Points are strictly inside the circle boundary"""
        c = Circle(x=0, y=0, radius=5)
        assert (point in c) is expected
        assert (Point(*point) in c) is expected

    def test_circle_contains_uses_center(self):
        """Containment is relative to the circle center"""
        c = Circle(x=10, y=10, radius=2)
        assert (11, 11) in c
        assert (0, 0) not in c

    @pytest.mark.parametrize("radius", [0, -5])
    def test_circle_without_positive_radius_contains_nothing(self, radius):
        """A circle with radius <= 0 contains no points"""
        assert (0, 0) not in Circle(radius=radius)

    def test_circle_exported_from_package(self):
        """Circle is importable from the top level package"""
        from twod import Circle as ExportedCircle

        assert ExportedCircle is Circle

    def test_circle_contains_rejects_other_types(self):
        """Unconvertible operands raise TypeError"""
        with pytest.raises(TypeError):
            "foo" in Circle(radius=5)

    def test_circle_negative_radius(self):
        """Test circle with negative radius"""
        c = Circle(radius=-5)
        assert c.radius == -5

    def test_circle_zero_radius(self):
        """Test circle with zero radius"""
        c = Circle(radius=0)
        assert c.radius == 0


def test_eccentricity_minor_longer_than_major_raises():
    e = Ellipse(minor_axis=5, major_axis=3)
    with pytest.raises(ValueError, match="longer than"):
        _ = e.e
