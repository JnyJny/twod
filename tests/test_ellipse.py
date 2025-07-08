"""Tests for ellipse.py module"""

import pytest
import math
from twod import Point
from twod.ellipse import Ellipse, Circle


class TestEllipse:
    """Test cases for Ellipse class"""

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

    def test_ellipse_inherits_from_point(self):
        """Test that Ellipse inherits Point functionality"""
        e = Ellipse(x=2, y=3, minor_axis=4, major_axis=6)
        assert isinstance(e, Point)
        assert e.radius == math.hypot(2, 3)
        assert e.xy == (2, 3)

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
        
        focus1 = e.focus1
        focus2 = e.focus2
        
        assert focus1.x == expected_e
        assert focus1.y == 3
        assert focus2.x == -expected_e
        assert focus2.y == 3

    def test_vertices(self):
        """Test vertices calculation"""
        e = Ellipse(x=2, y=3, minor_axis=3, major_axis=5)
        vertices = e.vertices
        
        assert len(vertices) == 2
        assert vertices[0] == Point(2 + 5, 3)  # (7, 3)
        assert vertices[1] == Point(-(2 + 5), 3)  # (-7, 3)

    def test_co_vertices(self):
        """Test co-vertices calculation"""
        e = Ellipse(x=2, y=3, minor_axis=3, major_axis=5)
        co_vertices = e.co_vertices
        
        assert len(co_vertices) == 2
        assert co_vertices[0] == Point(2, 3 + 3)  # (2, 6)
        assert co_vertices[1] == Point(2, -(3 + 3))  # (2, -6)

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

    def test_contains_method_exists(self):
        """Test that __contains__ method exists but is not implemented"""
        e = Ellipse(minor_axis=3, major_axis=5)
        point = Point(1, 1)
        result = e.__contains__(point)
        assert result is None

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

    def test_circle_inherits_from_point(self):
        """Test that Circle inherits Point functionality"""
        c = Circle(x=3, y=4, radius=5)
        assert isinstance(c, Point)
        assert c.distance() == math.hypot(3, 4)
        assert c.xy == (3, 4)

    def test_circle_contains_method_exists(self):
        """Test that __contains__ method exists but is not implemented"""
        c = Circle(x=0, y=0, radius=5)
        point = Point(1, 1)
        result = c.__contains__(point)
        assert result is None

    def test_circle_negative_radius(self):
        """Test circle with negative radius"""
        c = Circle(radius=-5)
        assert c.radius == -5

    def test_circle_zero_radius(self):
        """Test circle with zero radius"""
        c = Circle(radius=0)
        assert c.radius == 0