"""test Point multiplication like a human™"""

import pytest
from twod import CPoint as Point


@pytest.mark.parametrize(
    "A, B, result",
    [
        [[0, 0], [0, 0], [0, 0]],
        [[0, 0], [1, 1], [0, 0]],
        [[1, 1], [0, 0], [0, 0]],
        [[1, 1], [1, 1], [1, 1]],
    ],
)
def test_point_multiplication_with_point(A, B, result):
    p = Point(*A)
    q = Point(*B)
    r = p * q
    assert r == result


@pytest.mark.parametrize(
    "A, iterable, result",
    [
        [[0, 0], [0, 0], [0, 0]],
        [[0, 0], [1, 1], [0, 0]],
        [[1, 1], [0, 0], [0, 0]],
        [[1, 1], [1, 1], [1, 1]],
        [[0, 0], (0, 0), [0, 0]],
        [[0, 0], (1, 1), [0, 0]],
        [[1, 1], (0, 0), [0, 0]],
        [[1, 1], (1, 1), [1, 1]],
    ],
)
def test_point_multiplication_with_iterable(A, iterable, result):
    p = Point(*A) * iterable
    assert p == result


@pytest.mark.parametrize(
    "A, scalar, result",
    [
        [[0, 0], 1, [0, 0]],
    ],
)
def test_point_multiplication_with_scalar(A, scalar, result):
    p = Point(*A) * scalar
    assert p == result
