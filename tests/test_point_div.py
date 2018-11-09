import pytest

from twod import Point


def test_point_division_with_zero_points():
    p = Point()
    q = Point()
    with pytest.raises(ZeroDivisionError):
        r = p / q


def test_point_division_with_nonzero_points():
    p = Point(1, 1)
    q = Point(1, 1)

    r = p / q
    assert r.x == 1 and r.y == 1


def test_point_division_with_scalars():
    p = Point(1, 1) / 1
    assert p.x == 1 and p.y == 1


def test_point_inplace_division_with_zero_points():
    p = Point(1, 1)
    p /= Point(1, 1)
    assert p.x == 1 and p.y == 1


def test_point_inplace_division_with_nonzero_points():
    p = Point(2, 4)
    p /= Point(2, 2)
    assert p.x == 1 and p.y == 2


def test_point_inplace_division_with_scalars():

    p = Point(2, 4)
    p /= 2
    assert p.x == 1 and p.y == 2
