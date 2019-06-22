import pytest

from twod.point import Point
from twod.rect import Rect


def test_rect_creation_no_args():
    r = Rect()
    assert r.x == 0 and r.y == 0 and r.w == 0 and r.h == 0


def test_rect_creation_x_args():
    r = Rect(1)
    q = Rect(x=2)
    assert r.x == 1 and r.y == 0 and r.w == 0 and r.h == 0
    assert q.x == 2 and q.y == 0 and q.w == 0 and q.h == 0


def test_rect_creation_y_arg():
    r = Rect(y=1)
    assert r.x == 0 and r.y == 1 and r.w == 0 and r.h == 0


def test_rect_creation_xy_args():
    r = Rect(1, 2)
    assert r.x == 1 and r.y == 2 and r.w == 0 and r.h == 0


def test_rect_creation_wh_args():
    r = Rect(w=1, h=2)
    assert r.x == 0 and r.y == 0 and r.w == 1 and r.h == 2


def test_rect_creation_all_args():
    r = Rect(1, 2, 3, 4)
    assert r.x == 1 and r.y == 2 and r.w == 3 and r.h == 4


def test_rect_equality_empty():
    r = Rect()
    q = Rect()
    assert r == q


def test_rect_equality_nonempty():
    r = Rect(1, 2, 3, 4)
    q = Rect(1, 2, 3, 4)
    assert r == q


def test_rect_vertex_properties():
    r = Rect(1, 2, 3, 4)
    expected = [(1, 2), (4, 2), (4, 6), (1, 6)]

    assert tuple(r.A) == expected[0]
    assert tuple(r.B) == expected[1]
    assert tuple(r.C) == expected[2]
    assert tuple(r.D) == expected[3]

    for vertex, value in zip(r.vertices, expected):
        assert tuple(vertex) == value


def test_rect_sides():
    expected = [10, 5, 10, 5]

    assert Rect(w=10, h=5).sides == expected
    assert Rect(w=5, h=10).sides == expected[::-1]


def test_rect_perimeter():
    assert Rect().perimeter == 0
    assert Rect(w=1, h=1).perimeter == 4
    assert Rect(1, 2, 3, 4).perimeter == 14


def test_rect_area():
    assert Rect().area == 0
    assert Rect(w=1, h=1).area == 1
    assert Rect(1, 2, 3, 4).area == 12


def test_rect_center_getter():

    assert Rect().center == Point()
    assert Rect(w=2, h=2).center == Point(1, 1)
    assert Rect(1, 2, 3, 4).center == Point(2.5, 4)


def test_rect_center_setter():

    r = Rect(0, 0, w=2, h=2)
    q = Rect(0, 0, w=2, h=2)

    assert r.center == q.center

    new_center = (0, 0)

    r.center = new_center

    assert r.center != q.center and r.center == Point(*new_center)
    assert r.A == Point(-1, -1)
    assert r.B == Point(1, -1)
    assert r.C == Point(1, 1)
    assert r.D == Point(-1, 1)

    assert r.perimeter == q.perimeter
    assert r.area == q.area
    assert r.sides == q.sides
