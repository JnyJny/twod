"""Tests for Point.from_any() method to improve coverage"""

import pytest
from twod import Point


class TestPointFromAny:
    """Test cases for Point.from_any() method"""

    def test_from_any_cpoint_instance(self):
        """Test from_any with Point instance"""
        original = Point(1, 2)
        result = Point.from_any(original)
        assert result is original
        assert result.x == 1
        assert result.y == 2

    def test_from_any_complex_number(self):
        """Test from_any with complex number"""
        z = complex(3, 4)
        result = Point.from_any(z)
        assert result.x == 3
        assert result.y == 4

    def test_from_any_dict(self):
        """Test from_any with dictionary"""
        d = {"x": 5, "y": 6}
        result = Point.from_any(d)
        assert result.x == 5
        assert result.y == 6

    def test_from_any_list_cartesian(self):
        """Test from_any with list in cartesian coordinates"""
        coords = [7, 8]
        result = Point.from_any(coords)
        assert result.x == 7
        assert result.y == 8

    def test_from_any_tuple_cartesian(self):
        """Test from_any with tuple in cartesian coordinates"""
        coords = (9, 10)
        result = Point.from_any(coords)
        assert result.x == 9
        assert result.y == 10

    def test_from_any_list_polar(self):
        """Test from_any with list in polar coordinates"""
        import math

        radius, theta = 5, math.pi / 4
        result = Point.from_any([radius, theta], is_polar=True)
        expected_x = radius * math.cos(theta)
        expected_y = radius * math.sin(theta)
        assert abs(result.x - expected_x) < 1e-10
        assert abs(result.y - expected_y) < 1e-10

    def test_from_any_tuple_polar(self):
        """Test from_any with tuple in polar coordinates"""
        import math

        radius, theta = 3, math.pi / 6
        result = Point.from_any((radius, theta), is_polar=True)
        expected_x = radius * math.cos(theta)
        expected_y = radius * math.sin(theta)
        assert abs(result.x - expected_x) < 1e-10
        assert abs(result.y - expected_y) < 1e-10

    def test_from_any_float_scalar_ok(self):
        """Test from_any with float when scalar_ok=True"""
        result = Point.from_any(2.5, scalar_ok=True)
        assert result.x == 2.5
        assert result.y == 2.5

    def test_from_any_int_scalar_ok(self):
        """Test from_any with int when scalar_ok=True"""
        result = Point.from_any(3, scalar_ok=True)
        assert result.x == 3
        assert result.y == 3

    def test_from_any_float_scalar_not_ok(self):
        """Test from_any with float when scalar_ok=False"""
        with pytest.raises(TypeError):
            Point.from_any(2.5, scalar_ok=False)

    def test_from_any_int_scalar_not_ok(self):
        """Test from_any with int when scalar_ok=False"""
        with pytest.raises(TypeError):
            Point.from_any(3, scalar_ok=False)

    def test_from_any_string_valid_complex(self):
        """Test from_any with valid complex string"""
        result = Point.from_any("1+2j")
        assert result.x == 1
        assert result.y == 2

    def test_from_any_string_valid_complex_negative(self):
        """Test from_any with valid complex string with negative imaginary"""
        result = Point.from_any("3-4j")
        assert result.x == 3
        assert result.y == -4

    def test_from_any_string_valid_complex_pure_imaginary(self):
        """Test from_any with pure imaginary string"""
        result = Point.from_any("5j")
        assert result.x == 0
        assert result.y == 5

    def test_from_any_string_valid_complex_pure_real(self):
        """Test from_any with pure real string"""
        result = Point.from_any("7")
        assert result.x == 7
        assert result.y == 0

    def test_from_any_string_invalid(self):
        """Test from_any with invalid string"""
        with pytest.raises(TypeError):
            Point.from_any("invalid")

    def test_from_any_string_empty(self):
        """Test from_any with empty string"""
        with pytest.raises(TypeError):
            Point.from_any("")

    def test_from_any_unsupported_type(self):
        """Test from_any with unsupported type"""
        with pytest.raises(TypeError):
            Point.from_any(object())

    def test_from_any_none(self):
        """Test from_any with None"""
        with pytest.raises(TypeError):
            Point.from_any(None)

    def test_from_any_bool(self):
        """Test from_any with boolean (should be treated as int)"""
        result = Point.from_any(True, scalar_ok=True)
        assert result.x == 1
        assert result.y == 1

    def test_from_any_dict_missing_keys(self):
        """Test from_any with dict missing keys"""
        with pytest.raises(KeyError):
            Point.from_any({"x": 1})  # missing y

    def test_from_any_list_insufficient_elements(self):
        """Test from_any with list having insufficient elements"""
        with pytest.raises(IndexError):
            Point.from_any([1])  # only one element

    def test_from_any_empty_list(self):
        """Test from_any with empty list"""
        with pytest.raises(IndexError):
            Point.from_any([])
