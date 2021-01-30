"""testing Point addition like a human™
"""
import pytest

from twod import Point


@pytest.mark.parametrize(
    "A, B, result",
    [
        [[0, 0], [0, 0], (0, 0)],
        [[0, 0], [1, 1], (1, 1)],
        [[0, 0], [-1, -1], (-1, -1)],
        [[1, 1], [-1, -1], (0, 0)],
    ],
)
def test_point_addition_with_point(A, B, result):
    r = Point(*A) + Point(*B)
    assert r == result


@pytest.mark.parametrize(
    "A, scalar, result",
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
def test_point_addition_with_scalar(A, scalar, result):
    p = Point(*A) + scalar
    assert p == result


@pytest.mark.parametrize(
    "A, iterable, result",
    [
        [(0, 0), [1, 1], (1, 1)],
        [(0, 0), (2, 2), (2, 2)],
        [(0, 0), [3, 2, 1], (3, 2)],
    ],
)
def test_point_addition_with_iterable(A, iterable, result):
    r = Point(*A) + iterable
    assert r == result


@pytest.mark.parametrize(
    "A, B, result",
    [
        [[0, 0], [0, 0], (0, 0)],
        [[1, 2], [2, 3], [3, 5]],
    ],
)
def test_point_inplace_addition_with_point(A, B, result):
    p = Point(*A)
    p += Point(*B)
    assert p == result


@pytest.mark.parametrize(
    "A, iterable, result",
    [
        [(0, 0), [1, 1], (1, 1)],
        [(0, 0), (2, 2), (2, 2)],
        [(0, 0), [3, 2, 1], (3, 2)],
    ],
)
def test_point_inplace_addition_with_iterable(A, iterable, result):
    r = Point(*A)
    r += iterable
    assert r == result


@pytest.mark.parametrize(
    "A, scalar, result",
    [
        [[0, 0], 1, [1, 1]],
    ],
)
def test_point_inplace_addition_with_scalar(A, scalar, result):
    p = Point(*A)
    p += scalar
    assert p == result
