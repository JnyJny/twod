import pytest

from twod import Point


def test_point_creation_without_args():
    p = Point()
    assert p.x == 0 and p.y == 0
    assert p.is_origin


def test_point_creation_with_x_arg():
    p = Point(1)
    q = Point(x=2)
    assert p.x == 1 and p.y == 0
    assert q.x == 2 and q.y == 0


def test_point_creation_with_y_arg():
    p = Point(y=1)
    assert p.x == 0 and p.y == 1


def test_point_create_with_two_args():
    p = Point(1, 2)
    assert p.x == 1 and p.y == 2
    assert not p.is_origin


def test_point_equality():
    p = Point(1, 1)
    r = Point(1, 1)
    assert p == r and p is not r


def test_point_inequality():
    p = Point()
    r = Point(1, 1)
    assert p != r and p is not r
