"""test CPoint floor division like a human™"""

import pytest
from twod import CPoint as Point


@pytest.mark.parametrize("zero", [0, 0.0, [0, 0], (0, 0), Point()])
def test_point_floordiv_by_zero(zero):
    with pytest.raises(ZeroDivisionError):
        Point(1, 1) // zero


@pytest.mark.parametrize(
    "A, B, expected",
    [
        [[0, 0], [1, 1], [0, 0]],
        [[5, 7], [2, 2], [2, 3]],
        [[-5, -7], [2, 2], [-3, -4]],
        [[5.5, 7.5], [2, 2], [2, 3]],
    ],
)
def test_point_floordiv_with_point(A, B, expected):
    assert Point(*A) // Point(*B) == expected


@pytest.mark.parametrize("operand", [[2, 3], (2, 3), {"x": 2, "y": 3}])
def test_point_floordiv_with_other_types(operand):
    assert Point(5, 7) // operand == [2, 2]


@pytest.mark.parametrize("scalar", [2, 2.0])
def test_point_floordiv_with_scalar(scalar):
    assert Point(5, 7) // scalar == [2, 3]


def test_point_floordiv_returns_new_point():
    p = Point(5, 7)
    result = p // 2
    assert result is not p
    assert p == [5, 7]


def test_point_floordiv_unsupported_type():
    with pytest.raises(TypeError):
        Point() // object()


def test_point_ifloordiv_with_point():
    p = Point(5, 7)
    q = p
    p //= Point(2, 2)
    assert p == [2, 3]
    assert p is q


def test_point_ifloordiv_with_scalar():
    p = Point(5, 7)
    p //= 2
    assert p == [2, 3]


@pytest.mark.parametrize("zero", [0, [0, 0], Point()])
def test_point_ifloordiv_by_zero(zero):
    p = Point(1, 1)
    with pytest.raises(ZeroDivisionError):
        p //= zero
