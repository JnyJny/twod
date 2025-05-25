"""test Point division like a human™"""

import pytest
from twod import CPoint as Point


@pytest.mark.parametrize("zero", [0, 0.0, [0, 0], (0, 0), Point()])
def test_point_truediv_by_zero(zero):
    with pytest.raises(ZeroDivisionError):
        Point() / zero


@pytest.mark.parametrize(
    "A, B, expected",
    [
        [[0, 0], [1, 1], [0, 0]],
        [[1, 1], [1, 1], [1, 1]],
    ],
)
def test_point_truediv_with_point(A, B, expected):
    result = Point(*A) / Point(*B)
    assert result == expected


@pytest.mark.parametrize(
    "A, iterable, expected",
    [
        [[0, 0], [1, 1], [0, 0]],
        [[1, 1], [1, 1], [1, 1]],
    ],
)
def test_point_truediv_with_iterable(A, iterable, expected):
    p = Point(*A)
    result = p / iterable
    assert result == expected


@pytest.mark.parametrize(
    "A, scalar, expected",
    [
        [[0, 0], 1, [0, 0]],
        [[1, 1], 1, [1, 1]],
    ],
)
def test_point_truediv_with_scalar(A, scalar, expected):
    p = Point(*A)
    result = p / scalar
    assert result == expected


# floordiv on complex numbers doesn't make sense
#
# @pytest.mark.parametrize("zero", [0, 0.0, [0, 0], (0, 0), Point()])
# def test_point_floordiv_by_zero(zero):
#    with pytest.raises(ZeroDivisionError):
#        Point() // zero
#
# @pytest.mark.parametrize(
#    "A, B, expected",
#    [
#        [[0, 0], [1, 1], [0, 0]],
#        [[1, 1], [1, 1], [1, 1]],
#    ],
# )
# def test_point_floordiv_with_point(A, B, expected):
#    result = Point(*A) // Point(*B)
#    assert result == expected
#
#
# @pytest.mark.parametrize(
#    "A, iterable, expected",
#    [
#        [[0, 0], [1, 1], [0, 0]],
#        [[1, 1], [1, 1], [1, 1]],
#    ],
# )
# def test_point_floordiv_with_iterable(A, iterable, expected):
#    p = Point(*A)
#    r = p // iterable
#    assert r == expected
#
#
# @pytest.mark.parametrize(
#    "A, scalar, expected",
#    [
#        [[0, 0], 1, [0, 0]],
#        [[1, 1], 1, [1, 1]],
#    ],
# )
# def test_point_floordiv_with_scalar(A, scalar, expected):
#    p = Point(*A)
#    r = p // scalar
#    assert r == expected
