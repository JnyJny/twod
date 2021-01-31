""" test in-place Point division like a human™
"""
import pytest

from twod import Point


@pytest.mark.parametrize("zero", [0, 0.0, [0, 0], (0, 0), Point()])
def test_point_inplace_truediv_by_zero(zero, point):
    with pytest.raises(ZeroDivisionError):
        point /= zero


@pytest.mark.parametrize(
    "A, B, expected",
    [
        [[0, 0], [1, 1], [0, 0]],
        [[1, 1], [1, 1], [1, 1]],
    ],
)
def test_point_inplace_truediv_with_point(A, B, expected):
    p = Point(*A)
    p /= Point(*B)
    assert p == expected


@pytest.mark.parametrize(
    "A, iterable, expected",
    [
        [[0, 0], [1, 1], [0, 0]],
        [[1, 1], [1, 1], [1, 1]],
    ],
)
def test_point_inplace_truediv_with_iterable(A, iterable, expected):
    p = Point(*A)
    p /= iterable
    assert p == expected


@pytest.mark.parametrize(
    "A, scalar, expected",
    [
        [[0, 0], 1, [0, 0]],
        [[1, 1], 1, [1, 1]],
    ],
)
def test_point_inplace_truediv_with_scalar(A, scalar, expected):
    p = Point(*A)
    p /= scalar
    assert p == expected


@pytest.mark.parametrize("zero", [0, 0.0, [0, 0], (0, 0), Point()])
def test_point_inplace_floordiv_by_zero(zero, point):
    with pytest.raises(ZeroDivisionError):
        point //= zero


@pytest.mark.parametrize(
    "A, B, expected",
    [
        [[0, 0], [1, 1], [0, 0]],
        [[1, 1], [1, 1], [1, 1]],
    ],
)
def test_point_inplace_floordiv_with_point(A, B, expected):
    p = Point(*A)
    p //= Point(*B)
    assert p == expected


@pytest.mark.parametrize(
    "A, iterable, expected",
    [
        [[0, 0], [1, 1], [0, 0]],
        [[1, 1], [1, 1], [1, 1]],
    ],
)
def test_point_inplace_floordiv_with_iterable(A, iterable, expected):
    p = Point(*A)
    p //= iterable
    assert p == expected


@pytest.mark.parametrize(
    "A, scalar, expected",
    [
        [[0, 0], 1, [0, 0]],
        [[1, 1], 1, [1, 1]],
    ],
)
def test_point_inplace_floordiv_with_scalar(A, scalar, expected):
    p = Point(*A)
    p //= scalar
    assert p == expected
