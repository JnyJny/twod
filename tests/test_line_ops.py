"""Tests for Line arithmetic and geometric operations"""

import pytest
import math
import operator
from twod import Point, Line


class TestLineArithmeticOperations:
    """Test cases for Line arithmetic operations with comprehensive coverage"""

    @pytest.fixture
    def sample_line(self):
        """Sample line for testing"""
        return Line(Point(1, 2), Point(3, 4))

    def test_add_operations(self, sample_line):
        """Test all addition operations"""
        # Add Point
        result = sample_line + Point(1, 1)
        assert result == Line(Point(2, 3), Point(4, 5))
        
        # Add tuple
        result = sample_line + (2, 3)
        assert result == Line(Point(3, 5), Point(5, 7))
        
        # Add list
        result = sample_line + [1, 2]
        assert result == Line(Point(2, 4), Point(4, 6))
        
        # Add scalar
        result = sample_line + 5
        assert result == Line(Point(6, 7), Point(8, 9))

    def test_subtract_operations(self, sample_line):
        """Test all subtraction operations"""
        # Subtract Point
        result = sample_line - Point(1, 1)
        assert result == Line(Point(0, 1), Point(2, 3))
        
        # Subtract tuple
        result = sample_line - (0, 1)
        assert result == Line(Point(1, 1), Point(3, 3))
        
        # Subtract scalar
        result = sample_line - 1
        assert result == Line(Point(0, 1), Point(2, 3))

    def test_multiply_operations(self, sample_line):
        """Test all multiplication operations"""
        # Multiply by Point
        result = sample_line * Point(2, 3)
        assert result == Line(Point(2, 6), Point(6, 12))
        
        # Multiply by tuple
        result = sample_line * (2, 2)
        assert result == Line(Point(2, 4), Point(6, 8))
        
        # Multiply by scalar
        result = sample_line * 3
        assert result == Line(Point(3, 6), Point(9, 12))

    def test_divide_operations(self, sample_line):
        """Test all division operations"""
        # Divide by Point
        result = sample_line / Point(1, 2)
        assert result == Line(Point(1, 1), Point(3, 2))
        
        # Divide by tuple
        result = sample_line / (1, 1)
        assert result == Line(Point(1, 2), Point(3, 4))
        
        # Divide by scalar
        line = Line(Point(4, 6), Point(8, 12))
        result = line / 2
        assert result == Line(Point(2, 3), Point(4, 6))

    def test_unary_operations(self, sample_line):
        """Test unary operations"""
        # Negation
        result = -sample_line
        assert result == Line(Point(-1, -2), Point(-3, -4))
        
        # Absolute value
        negative_line = Line(Point(-2, -3), Point(4, -5))
        result = abs(negative_line)
        assert result == Line(Point(2, 3), Point(4, 5))

    def test_arithmetic_with_invalid_types(self, sample_line):
        """Test arithmetic operations with invalid types"""
        # Addition
        assert sample_line._op("invalid", operator.add) is NotImplemented
        assert sample_line._op({"x": 1}, operator.add) is NotImplemented
        
        # Subtraction
        assert sample_line._op("invalid", operator.sub) is NotImplemented
        
        # Multiplication
        assert sample_line._op("invalid", operator.mul) is NotImplemented
        
        # Division
        assert sample_line._op("invalid", operator.truediv) is NotImplemented

    def test_arithmetic_edge_cases(self):
        """Test arithmetic edge cases"""
        # Zero-length line
        zero_line = Line(Point(1, 1), Point(1, 1))
        result = zero_line + Point(2, 3)
        assert result == Line(Point(3, 4), Point(3, 4))
        
        # Operations with zero
        line = Line(Point(5, 10), Point(15, 20))
        result = line * 0
        assert result == Line(Point(0, 0), Point(0, 0))


class TestLineGeometricOperations:
    """Test cases for advanced geometric operations"""

    def test_complex_intersection_scenarios(self):
        """Test complex intersection scenarios"""
        # T-intersection
        line1 = Line(Point(0, 0), Point(4, 0))
        line2 = Line(Point(2, -2), Point(2, 2))
        intersection = line1.intersection_point(line2)
        assert intersection is not None
        assert intersection == Point(2, 0)
        
        # Lines sharing endpoint
        line1 = Line(Point(0, 0), Point(2, 2))
        line2 = Line(Point(2, 2), Point(4, 0))
        intersection = line1.intersection_point(line2)
        assert intersection is not None
        assert intersection == Point(2, 2)
        
        # Nearly parallel lines (should not intersect)
        line1 = Line(Point(0, 0), Point(10, 0.0001))
        line2 = Line(Point(0, 1), Point(10, 1))
        assert line1.intersection_point(line2) is None

    def test_distance_calculations_edge_cases(self):
        """Test distance calculations with edge cases"""
        # Point at exact endpoint
        line = Line(Point(0, 0), Point(5, 0))
        assert line.distance_to_point(Point(0, 0)) == 0.0
        assert line.distance_to_point(Point(5, 0)) == 0.0
        
        # Point very close to line
        assert abs(line.distance_to_point(Point(2.5, 1e-10))) < 1e-9
        
        # Point far from line
        assert line.distance_to_point(Point(2.5, 100)) == 100.0

    def test_angle_calculations(self):
        """Test angle calculations between lines"""
        # 30-60-90 triangle angles
        line1 = Line(Point(0, 0), Point(2, 0))  # Horizontal
        line2 = Line(Point(0, 0), Point(1, math.sqrt(3)))  # 60 degrees
        
        angle = line1.angle_between(line2)
        expected_angle = math.pi / 3  # 60 degrees in radians
        assert abs(angle - expected_angle) < 1e-10
        
        # Obtuse angle (should return acute equivalent)
        line3 = Line(Point(0, 0), Point(-1, math.sqrt(3)))  # 120 degrees
        angle = line1.angle_between(line3)
        assert abs(angle - expected_angle) < 1e-10  # Should be 60 degrees

    def test_extension_edge_cases(self):
        """Test line extension edge cases"""
        # Extend by exact length
        line = Line(Point(0, 0), Point(3, 4))  # Length 5
        extended = line.extend(5)  # Double the length
        assert abs(extended.length - 10.0) < 1e-10
        
        # Extend beyond zero (negative extension larger than line)
        short_line = Line(Point(0, 0), Point(1, 0))
        shortened = short_line.extend(-2)  # Should go negative
        assert shortened.end.x < 0
        
        # Extend horizontal line
        h_line = Line(Point(0, 0), Point(5, 0))
        extended_h = h_line.extend(3)
        assert extended_h.end == Point(8, 0)
        
        # Extend vertical line
        v_line = Line(Point(0, 0), Point(0, 4))
        extended_v = v_line.extend(2)
        assert extended_v.end == Point(0, 6)

    def test_parameter_based_operations(self):
        """Test parameter-based point operations"""
        line = Line(Point(0, 0), Point(10, 10))
        
        # Test various parameter values
        assert line.point_at_parameter(0) == Point(0, 0)
        assert line.point_at_parameter(0.25) == Point(2.5, 2.5)
        assert line.point_at_parameter(0.5) == Point(5, 5)
        assert line.point_at_parameter(0.75) == Point(7.5, 7.5)
        assert line.point_at_parameter(1) == Point(10, 10)
        
        # Beyond line segment
        assert line.point_at_parameter(1.5) == Point(15, 15)
        assert line.point_at_parameter(-0.5) == Point(-5, -5)

    def test_line_relationships_precision(self):
        """Test line relationship detection with numerical precision"""
        # Nearly parallel lines
        line1 = Line(Point(0, 0), Point(10, 0))
        line2 = Line(Point(0, 1), Point(10, 1.0000000001))
        assert line1.parallel_to(line2)  # Should be considered parallel
        
        # Test that exactly perpendicular lines are detected
        line1 = Line(Point(0, 0), Point(1, 0))
        line2 = Line(Point(0, 0), Point(0, 1))
        assert line1.perpendicular_to(line2)

    def test_containment_with_tolerance(self):
        """Test point containment with various tolerances"""
        line = Line(Point(0, 0), Point(10, 0))
        
        # Point exactly on line
        assert line.contains_point(Point(5, 0))
        
        # Point slightly off line
        slightly_off = Point(5, 0.001)
        assert not line.contains_point(slightly_off)  # Default tolerance
        assert line.contains_point(slightly_off, tolerance=0.01)
        assert not line.contains_point(slightly_off, tolerance=0.0001)

    def test_closest_point_edge_cases(self):
        """Test closest point calculation edge cases"""
        # Point projects beyond start
        line = Line(Point(5, 5), Point(10, 5))
        closest = line.closest_point_on_line(Point(0, 8))
        assert closest == Point(5, 5)  # Should clamp to start
        
        # Point projects beyond end
        closest = line.closest_point_on_line(Point(15, 8))
        assert closest == Point(10, 5)  # Should clamp to end
        
        # Point projects onto middle
        closest = line.closest_point_on_line(Point(7.5, 8))
        assert closest == Point(7.5, 5)  # Should project onto line

    def test_degenerate_cases(self):
        """Test operations on degenerate (zero-length) lines"""
        point_line = Line(Point(5, 5), Point(5, 5))
        
        # All geometric properties
        assert point_line.length == 0
        assert point_line.is_point
        assert point_line.vector == Point(0, 0)
        assert point_line.direction == Point(0, 0)
        assert point_line.midpoint == Point(5, 5)
        
        # Operations that should handle degenerate cases
        assert point_line.distance_to_point(Point(8, 9)) == 5.0  # Distance to point
        assert point_line.closest_point_on_line(Point(8, 9)) == Point(5, 5)
        
        # Relationships with other lines
        normal_line = Line(Point(0, 0), Point(1, 1))
        assert not point_line.parallel_to(normal_line)
        assert not point_line.perpendicular_to(normal_line)
        assert point_line.angle_between(normal_line) == 0.0

    def test_numerical_stability(self):
        """Test numerical stability with very small and large numbers"""
        # Very small line
        tiny_line = Line(Point(0, 0), Point(1e-10, 1e-10))
        assert tiny_line.length > 0
        assert not tiny_line.is_point
        
        # Very large line
        huge_line = Line(Point(0, 0), Point(1e10, 1e10))
        assert huge_line.length > 1e10
        direction = huge_line.direction
        assert abs(direction.radius - 1.0) < 1e-10  # Should still be unit vector
        
        # Operations with mixed scales
        result = tiny_line.intersects_line(huge_line)
        assert isinstance(result, bool)  # Should not crash