"""testing Point addition like a human™
"""
import pytest

from twod import Point


@pytest.mark.parametrize(
    "A, B, expected",
    [
        [[0, 0], [0, 0], (0, 0)],
        [[0, 0], [1, 1], (1, 1)],
        [[0, 0], [-1, -1], (-1, -1)],
        [[1, 1], [-1, -1], (0, 0)],
    ],
)
def test_point_addition_with_point(A, B, expected):
    result = Point(*A) + Point(*B)
    assert result == expected


@pytest.mark.parametrize(
    "A, scalar, expected",
    [
        [[0, 0], -1, [-1, -1]],
        [[1, 1], -1, [0, 0]],
        [[0, 0], 1, [1, 1]],
        [[1, 1], 1, [2, 2]],
        [[0, 0], 0, [0, 0]],
        [[1, 1], 0, [1, 1]],
        [[0, 0], -1.0, [-1, -1]],
        [[1, 1], -1.0, [0, 0]],
        [[0, 0], 1.0, [1, 1]],
        [[1, 1], 1.0, [2, 2]],
        [[0, 0], 0.0, [0, 0]],
        [[1, 1], 0.0, [1, 1]],
    ],
)
def test_point_addition_with_scalar(A, scalar, expected):
    result = Point(*A) + scalar
    assert result == expected


@pytest.mark.parametrize(
    "A, iterable, expected",
    [
        [(0, 0), [1, 1], (1, 1)],
        [(0, 0), (2, 2), (2, 2)],
        [(0, 0), [3, 2, 1], (3, 2)],
    ],
)
def test_point_addition_with_iterable(A, iterable, expected):
    result = Point(*A) + iterable
    assert result == expected
