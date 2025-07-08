"""testing Point addition like a human™
"""
import pytest

from twod import CPoint as Point


@pytest.mark.parametrize(
    "A, B, expected",
    [
        [[0, 0], [0, 0], (0, 0)],
        [[1, 2], [2, 3], [3, 5]],
    ],
)
def test_point_inplace_addition_with_point(A, B, expected):
    p = Point(*A)
    p += Point(*B)
    assert p == expected


@pytest.mark.parametrize(
    "A, iterable, expected",
    [
        [(0, 0), [1, 1], (1, 1)],
        [(0, 0), (2, 2), (2, 2)],
        [(0, 0), [3, 2, 1], (3, 2)],
    ],
)
def test_point_inplace_addition_with_iterable(A, iterable, expected):
    r = Point(*A)
    r += iterable
    assert r == expected


@pytest.mark.parametrize(
    "A, scalar, expected",
    [
        [[0, 0], 1, [1, 1]],
    ],
)
def test_point_inplace_addition_with_scalar(A, scalar, expected):
    p = Point(*A)
    p += scalar
    assert p == expected