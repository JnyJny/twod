""" """

import pytest
from twod.point import Point
from twod.rect import Rect

A_RANGE = list(range(-10, 10))


def test_rect_creation_no_args() -> None:
    r = Rect()
    assert r.x == 0 and r.y == 0 and r.w == 0 and r.h == 0


@pytest.mark.parametrize("x", A_RANGE)
def test_rect_creation_x_args(x) -> None:
    r = Rect(x)
    q = Rect(x=x)
    assert r.x == x and r.y == 0 and r.w == 0 and r.h == 0
    assert q.x == x and q.y == 0 and q.w == 0 and q.h == 0


@pytest.mark.parametrize("y", A_RANGE)
def test_rect_creation_y_arg(y) -> None:
    r = Rect(y=y)
    assert r.x == 0 and r.y == y and r.w == 0 and r.h == 0


@pytest.mark.parametrize("x,y", list(zip(A_RANGE, A_RANGE)))
def test_rect_creation_xy_args(x, y) -> None:
    r = Rect(x, y)
    assert r.x == x and r.y == y and r.w == 0 and r.h == 0


@pytest.mark.parametrize("w,h", list(zip(A_RANGE, A_RANGE)))
def test_rect_creation_wh_args(w, h) -> None:
    r = Rect(w=w, h=h)
    assert r.x == 0 and r.y == 0 and r.w == w and r.h == h


@pytest.mark.parametrize("x,y,w,h", list(zip(A_RANGE, A_RANGE, A_RANGE, A_RANGE)))
def test_rect_creation_all_args(x, y, w, h) -> None:
    r = Rect(x, y, w, h)
    assert r.x == x and r.y == y and r.w == w and r.h == h


def test_rect_equality_empty() -> None:
    r = Rect()
    q = Rect()
    assert r == q
    assert r == r
    assert q == r
    assert q == q


@pytest.mark.parametrize("x,y,w,h", list(zip(A_RANGE, A_RANGE, A_RANGE, A_RANGE)))
def test_rect_equality_nonempty(x, y, w, h) -> None:
    r = Rect(x, y, w, h)
    q = Rect(x, y, w, h)
    assert r == q
    assert r == r
    assert q == r
    assert q == q


@pytest.mark.parametrize(
    "x,y,w,h, A, B, C, D",
    [
        (1, 2, 3, 4, (1, 2), (4, 2), (4, 6), (1, 6)),
    ],
)
def test_rect_vertex_properties(x, y, w, h, A, B, C, D) -> None:
    r = Rect(x, y, w, h)

    assert tuple(r.A) == A
    assert tuple(r.B) == B
    assert tuple(r.C) == C
    assert tuple(r.D) == D

    for vertex, value in zip(r.vertices, [A, B, C, D]):
        assert tuple(vertex) == value


def test_rect_sides() -> None:
    expected = [10, 5, 10, 5]

    assert Rect(w=10, h=5).sides == expected
    assert Rect(w=5, h=10).sides == expected[::-1]


@pytest.mark.parametrize(
    "x,y,w,h,expected",
    [
        (0, 0, 0, 0, 0),
        (0, 0, 1, 1, 4),
        (1, 2, 3, 4, 14),
    ],
)
def test_rect_perimeter(x, y, w, h, expected) -> None:
    assert Rect(x, y, w, h).perimeter == expected


@pytest.mark.parametrize(
    "x,y,w,h,expected",
    [
        (0, 0, 0, 0, 0),
        (0, 0, 1, 1, 1),
        (1, 2, 3, 4, 12),
    ],
)
def test_rect_area(x, y, w, h, expected) -> None:
    assert Rect(x, y, w, h).area == expected


@pytest.mark.parametrize(
    "x,y,w,h,expected",
    [
        (0, 0, 0, 0, Point()),
        (0, 0, 2, 2, Point(1, 1)),
        (1, 2, 3, 4, Point(2.5, 4)),
    ],
)
def test_rect_center_getter(x, y, w, h, expected):
    assert Rect(x, y, w, h).center == expected


def test_rect_center_setter() -> None:

    r = Rect(0, 0, w=2, h=2)
    q = Rect(0, 0, w=2, h=2)

    assert r.center == q.center
    assert r.perimeter == q.perimeter
    assert r.area == q.area
    assert r.sides == q.sides

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
