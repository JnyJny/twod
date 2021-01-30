"""testing Point subtraction like a human™
"""
import pytest

from twod import Point


@pytest.mark.parametrize(
    "A, B, result",
    [
        [[0, 0], [0, 0], (0, 0)],
        [[0, 0], [1, 1], (-1, -1)],
        [[0, 0], [-1, -1], (1, 1)],
        [[1, 1], [-1, -1], (2, 2)],
    ],
)
def test_point_subtraction_with_point(A, B, result):
    r = Point(*A) - Point(*B)
    assert r == result


@pytest.mark.parametrize(
    "A, scalar, result",
    [
        [[0, 0], -1, [1, 1]],
        [[1, 1], -1, [2, 2]],
        [[0, 0], 1, [-1, -1]],
        [[1, 1], 1, [0, 0]],
        [[0, 0], 0, [0, 0]],
        [[1, 1], 0, [1, 1]],
        [[0, 0], -1.0, [1, 1]],
        [[1, 1], -1.0, [2, 2]],
        [[0, 0], 1.0, [-1, -1]],
        [[1, 1], 1.0, [0, 0]],
        [[0, 0], 0.0, [0, 0]],
        [[1, 1], 0.0, [1, 1]],
    ],
)
def test_point_subtraction_with_scalar(A, scalar, result):
    p = Point(*A) - scalar
    assert p == result


@pytest.mark.parametrize(
    "A, values, result",
    [
        [(0, 0), [1, 1], (-1, -1)],
        [(0, 0), (2, 2), (-2, -2)],
        [(0, 0), [3, 2, 1], (-3, -2)],
    ],
)
def test_point_subtraction_with_iterable(A, values, result):
    r = Point(*A) - values
    assert r == result


@pytest.mark.parametrize(
    "A, B, result",
    [
        [[0, 0], [0, 0], (0, 0)],
        [[1, 2], [2, 3], [-1, -1]],
    ],
)
def test_point_inplace_subtraction_with_point(A, B, result):
    p = Point(*A)
    p -= Point(*B)
    assert p == result


@pytest.mark.parametrize(
    "A, values, result",
    [
        [(0, 0), [1, 1], (-1, -1)],
        [(0, 0), (2, 2), (-2, -2)],
        [(0, 0), [3, 2, 1], (-3, -2)],
    ],
)
def test_point_inplace_subtraction_with_iterable(A, values, result):
    r = Point(*A)
    r -= values
    assert r == result


@pytest.mark.parametrize(
    "A, scalar, result",
    [
        [[0, 0], 1, [-1, -1]],
    ],
)
def test_point_inplace_subtraction_with_scalar(A, scalar, result):
    p = Point(*A)
    p -= scalar
    assert p == result
