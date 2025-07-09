"""Tests for line.py module"""

import pytest
import math
import operator
from twod import Point, Line


class TestLineCreation:
    """Test cases for Line creation and basic properties"""

    def test_line_creation_default(self):
        """Test default line creation"""
        line = Line()
        assert line.start == Point(0, 0)
        assert line.end == Point(0, 0)
        assert line.is_point

    def test_line_creation_with_points(self):
        """Test line creation with Point objects"""
        start = Point(1, 2)
        end = Point(4, 6)
        line = Line(start, end)
        assert line.start == start
        assert line.end == end

    def test_line_creation_with_tuples(self):
        """Test line creation with tuple coordinates"""
        line = Line((1, 2), (4, 6))
        assert line.start == Point(1, 2)
        assert line.end == Point(4, 6)

    def test_line_creation_with_mixed_types(self):
        """Test line creation with mixed Point and tuple"""
        line = Line(Point(1, 2), (4, 6))
        assert line.start == Point(1, 2)
        assert line.end == Point(4, 6)

    def test_line_creation_with_scalars(self):
        """Test line creation with scalar values"""
        line = Line(5, 10)
        assert line.start == Point(5, 0)
        assert line.end == Point(10, 0)


class TestLineProperties:
    """Test cases for Line properties"""

    def test_length_horizontal(self):
        """Test length of horizontal line"""
        line = Line(Point(0, 0), Point(3, 0))
        assert line.length == 3.0

    def test_length_vertical(self):
        """Test length of vertical line"""
        line = Line(Point(0, 0), Point(0, 4))
        assert line.length == 4.0

    def test_length_diagonal(self):
        """Test length of diagonal line (3-4-5 triangle)"""
        line = Line(Point(0, 0), Point(3, 4))
        assert line.length == 5.0

    def test_length_squared(self):
        """Test squared length calculation"""
        line = Line(Point(0, 0), Point(3, 4))
        assert line.length_squared == 25.0

    def test_vector(self):
        """Test vector property"""
        line = Line(Point(1, 2), Point(4, 6))
        assert line.vector == Point(3, 4)

    def test_direction_unit_vector(self):
        """Test direction unit vector"""
        line = Line(Point(0, 0), Point(3, 4))
        direction = line.direction
        assert abs(direction.radius - 1.0) < 1e-10
        assert direction.x == 0.6
        assert direction.y == 0.8

    def test_direction_zero_length(self):
        """Test direction for zero-length line"""
        line = Line(Point(1, 1), Point(1, 1))
        assert line.direction == Point(0, 0)

    def test_angle_radians(self):
        """Test angle in radians"""
        line = Line(Point(0, 0), Point(1, 0))
        assert line.angle_radians == 0.0
        
        line = Line(Point(0, 0), Point(0, 1))
        assert abs(line.angle_radians - math.pi/2) < 1e-10

    def test_angle_degrees(self):
        """Test angle in degrees"""
        line = Line(Point(0, 0), Point(1, 0))
        assert line.angle_degrees == 0.0
        
        line = Line(Point(0, 0), Point(0, 1))
        assert abs(line.angle_degrees - 90.0) < 1e-10

    def test_slope_horizontal(self):
        """Test slope of horizontal line"""
        line = Line(Point(0, 5), Point(10, 5))
        assert line.slope == 0.0

    def test_slope_vertical(self):
        """Test slope of vertical line"""
        line = Line(Point(5, 0), Point(5, 10))
        assert line.slope == float('inf')
        
        line = Line(Point(5, 10), Point(5, 0))
        assert line.slope == float('-inf')

    def test_slope_diagonal(self):
        """Test slope of diagonal line"""
        line = Line(Point(0, 0), Point(2, 4))
        assert line.slope == 2.0

    def test_midpoint(self):
        """Test midpoint calculation"""
        line = Line(Point(0, 0), Point(4, 6))
        assert line.midpoint == Point(2, 3)

    def test_is_point_true(self):
        """Test is_point for zero-length line"""
        line = Line(Point(1, 2), Point(1, 2))
        assert line.is_point

    def test_is_point_false(self):
        """Test is_point for non-zero line"""
        line = Line(Point(0, 0), Point(1, 0))
        assert not line.is_point

    def test_is_horizontal(self):
        """Test horizontal line detection"""
        line = Line(Point(0, 5), Point(10, 5))
        assert line.is_horizontal
        
        line = Line(Point(0, 0), Point(0, 5))
        assert not line.is_horizontal

    def test_is_vertical(self):
        """Test vertical line detection"""
        line = Line(Point(5, 0), Point(5, 10))
        assert line.is_vertical
        
        line = Line(Point(0, 0), Point(5, 0))
        assert not line.is_vertical


class TestLineOperations:
    """Test cases for Line operations"""

    def test_reverse(self):
        """Test line reversal"""
        line = Line(Point(1, 2), Point(3, 4))
        reversed_line = line.reverse()
        assert reversed_line.start == Point(3, 4)
        assert reversed_line.end == Point(1, 2)

    def test_extend_from_end(self):
        """Test extending line from end"""
        line = Line(Point(0, 0), Point(3, 4))
        extended = line.extend(5)  # Total length should be 10
        assert abs(extended.length - 10.0) < 1e-10
        assert extended.start == Point(0, 0)

    def test_extend_from_start(self):
        """Test extending line from start"""
        line = Line(Point(0, 0), Point(3, 4))
        extended = line.extend(5, from_end=False)
        assert abs(extended.length - 10.0) < 1e-10
        assert extended.end == Point(3, 4)

    def test_extend_negative(self):
        """Test extending line with negative distance (shortening)"""
        line = Line(Point(0, 0), Point(5, 0))
        shortened = line.extend(-2)
        assert shortened.length == 3.0
        assert shortened.start == Point(0, 0)
        assert shortened.end == Point(3, 0)

    def test_extend_zero_length(self):
        """Test extending zero-length line"""
        line = Line(Point(1, 1), Point(1, 1))
        extended = line.extend(5)
        assert extended.start == Point(1, 1)
        assert extended.end == Point(1, 1)

    def test_point_at_parameter(self):
        """Test getting point at parameter t"""
        line = Line(Point(0, 0), Point(10, 0))
        assert line.point_at_parameter(0) == Point(0, 0)
        assert line.point_at_parameter(1) == Point(10, 0)
        assert line.point_at_parameter(0.5) == Point(5, 0)
        assert line.point_at_parameter(2) == Point(20, 0)  # Beyond end

    def test_distance_to_point_on_line(self):
        """Test distance to point that lies on the line"""
        line = Line(Point(0, 0), Point(10, 0))
        assert line.distance_to_point(Point(5, 0)) == 0.0

    def test_distance_to_point_perpendicular(self):
        """Test distance to point perpendicular to line"""
        line = Line(Point(0, 0), Point(10, 0))
        assert line.distance_to_point(Point(5, 3)) == 3.0

    def test_distance_to_point_beyond_endpoints(self):
        """Test distance to point beyond line endpoints"""
        line = Line(Point(0, 0), Point(5, 0))
        assert line.distance_to_point(Point(10, 0)) == 5.0  # Distance to end point

    def test_distance_to_point_zero_length(self):
        """Test distance to point for zero-length line"""
        line = Line(Point(1, 1), Point(1, 1))
        assert line.distance_to_point(Point(4, 5)) == 5.0

    def test_closest_point_on_line(self):
        """Test finding closest point on line"""
        line = Line(Point(0, 0), Point(10, 0))
        assert line.closest_point_on_line(Point(5, 3)) == Point(5, 0)
        assert line.closest_point_on_line(Point(-2, 0)) == Point(0, 0)  # Clamped to start
        assert line.closest_point_on_line(Point(15, 0)) == Point(10, 0)  # Clamped to end


class TestLineIntersections:
    """Test cases for Line intersections"""

    def test_intersects_line_crossing(self):
        """Test intersection of crossing lines"""
        line1 = Line(Point(0, 0), Point(2, 2))
        line2 = Line(Point(0, 2), Point(2, 0))
        assert line1.intersects_line(line2)

    def test_intersects_line_parallel(self):
        """Test intersection of parallel lines"""
        line1 = Line(Point(0, 0), Point(2, 0))
        line2 = Line(Point(0, 1), Point(2, 1))
        assert not line1.intersects_line(line2)

    def test_intersects_line_collinear(self):
        """Test intersection of collinear lines"""
        line1 = Line(Point(0, 0), Point(2, 0))
        line2 = Line(Point(1, 0), Point(3, 0))
        assert not line1.intersects_line(line2)  # Parallel but collinear

    def test_intersection_point_crossing(self):
        """Test intersection point of crossing lines"""
        line1 = Line(Point(0, 0), Point(2, 2))
        line2 = Line(Point(0, 2), Point(2, 0))
        intersection = line1.intersection_point(line2)
        assert intersection is not None
        assert intersection == Point(1, 1)

    def test_intersection_point_parallel(self):
        """Test intersection point of parallel lines"""
        line1 = Line(Point(0, 0), Point(2, 0))
        line2 = Line(Point(0, 1), Point(2, 1))
        assert line1.intersection_point(line2) is None

    def test_intersection_point_non_intersecting(self):
        """Test intersection point of non-intersecting segments"""
        line1 = Line(Point(0, 0), Point(1, 0))
        line2 = Line(Point(2, 0), Point(3, 0))
        assert line1.intersection_point(line2) is None


class TestLineRelationships:
    """Test cases for Line relationships"""

    def test_parallel_to_true(self):
        """Test parallel line detection"""
        line1 = Line(Point(0, 0), Point(2, 0))
        line2 = Line(Point(0, 1), Point(2, 1))
        assert line1.parallel_to(line2)

    def test_parallel_to_false(self):
        """Test non-parallel line detection"""
        line1 = Line(Point(0, 0), Point(2, 0))
        line2 = Line(Point(0, 0), Point(0, 2))
        assert not line1.parallel_to(line2)

    def test_parallel_to_with_point(self):
        """Test parallel detection with zero-length line"""
        line1 = Line(Point(0, 0), Point(2, 0))
        line2 = Line(Point(1, 1), Point(1, 1))
        assert not line1.parallel_to(line2)

    def test_perpendicular_to_true(self):
        """Test perpendicular line detection"""
        line1 = Line(Point(0, 0), Point(2, 0))
        line2 = Line(Point(0, 0), Point(0, 2))
        assert line1.perpendicular_to(line2)

    def test_perpendicular_to_false(self):
        """Test non-perpendicular line detection"""
        line1 = Line(Point(0, 0), Point(2, 0))
        line2 = Line(Point(0, 0), Point(1, 1))
        assert not line1.perpendicular_to(line2)

    def test_angle_between_perpendicular(self):
        """Test angle between perpendicular lines"""
        line1 = Line(Point(0, 0), Point(1, 0))
        line2 = Line(Point(0, 0), Point(0, 1))
        angle = line1.angle_between(line2)
        assert abs(angle - math.pi/2) < 1e-10

    def test_angle_between_parallel(self):
        """Test angle between parallel lines"""
        line1 = Line(Point(0, 0), Point(1, 0))
        line2 = Line(Point(0, 1), Point(1, 1))
        angle = line1.angle_between(line2)
        assert abs(angle) < 1e-10

    def test_angle_between_45_degrees(self):
        """Test angle between 45-degree lines"""
        line1 = Line(Point(0, 0), Point(1, 0))
        line2 = Line(Point(0, 0), Point(1, 1))
        angle = line1.angle_between(line2)
        assert abs(angle - math.pi/4) < 1e-10

    def test_contains_point_true(self):
        """Test point containment on line"""
        line = Line(Point(0, 0), Point(4, 0))
        assert line.contains_point(Point(2, 0))

    def test_contains_point_false(self):
        """Test point not on line"""
        line = Line(Point(0, 0), Point(4, 0))
        assert not line.contains_point(Point(2, 1))

    def test_contains_point_endpoint(self):
        """Test endpoint containment"""
        line = Line(Point(0, 0), Point(4, 0))
        assert line.contains_point(Point(0, 0))
        assert line.contains_point(Point(4, 0))

    def test_contains_point_with_tolerance(self):
        """Test point containment with tolerance"""
        line = Line(Point(0, 0), Point(4, 0))
        assert line.contains_point(Point(2, 0.001), tolerance=0.01)
        assert not line.contains_point(Point(2, 0.1), tolerance=0.01)


class TestLineSpecialMethods:
    """Test cases for Line special methods"""

    def test_equality_true(self):
        """Test line equality"""
        line1 = Line(Point(1, 2), Point(3, 4))
        line2 = Line(Point(1, 2), Point(3, 4))
        assert line1 == line2

    def test_equality_false(self):
        """Test line inequality"""
        line1 = Line(Point(1, 2), Point(3, 4))
        line2 = Line(Point(1, 2), Point(4, 5))
        assert line1 != line2

    def test_equality_with_non_line(self):
        """Test equality with non-Line object"""
        line = Line(Point(1, 2), Point(3, 4))
        assert line != "not a line"

    def test_len(self):
        """Test line length (number of points)"""
        line = Line(Point(1, 2), Point(3, 4))
        assert len(line) == 2

    def test_getitem(self):
        """Test indexing line points"""
        line = Line(Point(1, 2), Point(3, 4))
        assert line[0] == Point(1, 2)
        assert line[1] == Point(3, 4)

    def test_getitem_out_of_range(self):
        """Test indexing out of range"""
        line = Line(Point(1, 2), Point(3, 4))
        with pytest.raises(IndexError):
            _ = line[2]

    def test_setitem(self):
        """Test setting line points"""
        line = Line(Point(1, 2), Point(3, 4))
        line[0] = Point(5, 6)
        line[1] = (7, 8)
        assert line.start == Point(5, 6)
        assert line.end == Point(7, 8)

    def test_setitem_out_of_range(self):
        """Test setting out of range index"""
        line = Line(Point(1, 2), Point(3, 4))
        with pytest.raises(IndexError):
            line[2] = Point(5, 6)

    def test_iter(self):
        """Test iterating over line points"""
        line = Line(Point(1, 2), Point(3, 4))
        points = list(line)
        assert points == [Point(1, 2), Point(3, 4)]


class TestLineArithmetic:
    """Test cases for Line arithmetic operations"""

    def test_add_point(self):
        """Test adding point to line"""
        line = Line(Point(1, 2), Point(3, 4))
        result = line + Point(1, 1)
        assert result == Line(Point(2, 3), Point(4, 5))

    def test_add_tuple(self):
        """Test adding tuple to line"""
        line = Line(Point(1, 2), Point(3, 4))
        result = line + (1, 1)
        assert result == Line(Point(2, 3), Point(4, 5))

    def test_add_scalar(self):
        """Test adding scalar to line"""
        line = Line(Point(1, 2), Point(3, 4))
        result = line + 2
        assert result == Line(Point(3, 4), Point(5, 6))

    def test_subtract_point(self):
        """Test subtracting point from line"""
        line = Line(Point(3, 4), Point(5, 6))
        result = line - Point(1, 1)
        assert result == Line(Point(2, 3), Point(4, 5))

    def test_multiply_scalar(self):
        """Test multiplying line by scalar"""
        line = Line(Point(1, 2), Point(3, 4))
        result = line * 2
        assert result == Line(Point(2, 4), Point(6, 8))

    def test_divide_scalar(self):
        """Test dividing line by scalar"""
        line = Line(Point(2, 4), Point(6, 8))
        result = line / 2
        assert result == Line(Point(1, 2), Point(3, 4))

    def test_negate(self):
        """Test negating line"""
        line = Line(Point(1, 2), Point(3, 4))
        result = -line
        assert result == Line(Point(-1, -2), Point(-3, -4))

    def test_absolute(self):
        """Test absolute value of line"""
        line = Line(Point(-1, -2), Point(3, -4))
        result = abs(line)
        assert result == Line(Point(1, 2), Point(3, 4))

    def test_arithmetic_not_implemented(self):
        """Test arithmetic with unsupported types"""
        line = Line(Point(1, 2), Point(3, 4))
        result = line._op("invalid", operator.add)
        assert result is NotImplemented