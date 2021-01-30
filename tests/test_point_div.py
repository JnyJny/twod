""" test Point division like a human™
"""
import pytest

from twod import Point


@pytest.mark.parametrize("zero", [0, 0.0, [0, 0], (0, 0), Point()])
def test_point_truediv_by_zero(zero):
    with pytest.raises(ZeroDivisionError):
        Point() / zero


@pytest.mark.parametrize(
    "A, B, result",
    [
        [[0, 0], [1, 1], [0, 0]],
        [[1, 1], [1, 1], [1, 1]],
    ],
)
def test_point_truediv_with_point(A, B, result):
    r = Point(*A) / Point(*B)
    assert r == result


@pytest.mark.parametrize(
    "A, iterable, result",
    [
        [[0, 0], [1, 1], [0, 0]],
        [[1, 1], [1, 1], [1, 1]],
    ],
)
def test_point_truediv_with_iterable(A, iterable, result):
    p = Point(*A)
    r = p / iterable
    assert r == result


@pytest.mark.parametrize(
    "A, scalar, result",
    [
        [[0, 0], 1, [0, 0]],
        [[1, 1], 1, [1, 1]],
    ],
)
def test_point_truediv_with_scalar(A, scalar, result):
    p = Point(*A)
    r = p / scalar
    assert result == result


@pytest.mark.parametrize("zero", [0, 0.0, [0, 0], (0, 0), Point()])
def test_point_floordiv_by_zero(zero):
    with pytest.raises(ZeroDivisionError):
        Point() // zero


@pytest.mark.parametrize(
    "A, B, result",
    [
        [[0, 0], [1, 1], [0, 0]],
        [[1, 1], [1, 1], [1, 1]],
    ],
)
def test_point_floordiv_with_point(A, B, result):
    r = Point(*A) // Point(*B)
    assert r == result


@pytest.mark.parametrize(
    "A, iterable, result",
    [
        [[0, 0], [1, 1], [0, 0]],
        [[1, 1], [1, 1], [1, 1]],
    ],
)
def test_point_floordiv_with_iterable(A, iterable, result):
    p = Point(*A)
    r = p // iterable
    assert r == result


@pytest.mark.parametrize(
    "A, scalar, result",
    [
        [[0, 0], 1, [0, 0]],
        [[1, 1], 1, [1, 1]],
    ],
)
def test_point_floordiv_with_scalar(A, scalar, result):
    p = Point(*A)
    r = p // scalar
    assert result == result
