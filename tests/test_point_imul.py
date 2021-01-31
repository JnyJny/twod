""" test in-place Point multiplication like a human™
"""

import pytest

from twod import Point


@pytest.mark.parametrize(
    "A, B, result",
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
def test_point_inplace_multiplication_with_point(A, B, result):
    p = Point(*A)
    p *= Point(*B)
    assert p == result


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
def test_point_inplace_multiplication_with_iterable(A, iterable, result):
    p = Point(*A)
    p *= iterable
    assert p == result


@pytest.mark.parametrize(
    "A, scalar, result",
    [
        [[0, 0], 1, [0, 0]],
    ],
)
def test_point_inplace_multiplication_with_scalar(A, scalar, result):

    p = Point(*A)
    p *= scalar
    assert p == result
