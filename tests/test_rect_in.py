""" """

import pytest
from twod import Point, Rect

# EJO Needs more literal edge case testing where points are on the
#     edges of a rectangle.


def test_point_in_rect() -> None:
    p = Point(1, 1)
    bb = Rect(0, 0, 2, 2)
    assert p in bb


def test_point_not_in_rect() -> None:
    p = Point()
    bb = Rect(1, 1, 2, 2)
    assert p not in bb


def test_embedded_rect_in_rect() -> None:
    bb = Rect(1, 1, 1, 1)
    qq = Rect(0, 0, 3, 3)
    assert bb in qq
    assert qq not in bb


def test_rect_not_in_rect() -> None:
    bb = Rect(0, 0, 1, 1)
    qq = Rect(10, 10, 1, 1)
    assert bb not in qq
    assert qq not in bb


@pytest.mark.parametrize(
    "a,b",
    [
        (Rect(0, 0, 1, 1), Rect(0, 1, 1, 1)),
        (Rect(0, 0, 1, 1), Rect(1, 0, 1, 1)),
        (Rect(0, 0, 1, 1), Rect(1, 1, 1, 1)),
        (Rect(0, 0, 1, 1), Rect(0, -1, 1, 1)),
        (Rect(0, 0, 1, 1), Rect(-1, 0, 1, 1)),
        (Rect(0, 0, 1, 1), Rect(-1, -1, 1, 1)),
        (Rect(0, 1, 1, 1), Rect(0, 0, 1, 1)),
        (Rect(1, 0, 1, 1), Rect(0, 0, 1, 1)),
        (Rect(1, 1, 1, 1), Rect(0, 0, 1, 1)),
        (Rect(0, -1, 1, 1), Rect(0, 0, 1, 1)),
        (Rect(-1, 0, 1, 1), Rect(0, 0, 1, 1)),
        (Rect(-1, -1, 1, 1), Rect(0, 0, 1, 1)),
    ],
)
def test_rect_adjacent_to_rect(a: Rect, b: Rect) -> None:
    assert a not in b
    assert b not in a


def test_same_rect_inside() -> None:
    r = Rect(0, 0, 1, 1)
    assert r not in r


def test_rect_in_rect_requires_full_containment() -> None:
    outer = Rect(0, 0, 10, 10)
    assert Rect(2, 2, 3, 3) in outer
    assert Rect(8, 8, 5, 5) not in outer
    assert Rect(-5, -5, 20, 20) not in outer


def test_rect_in_rect_cross_overlap_is_not_containment() -> None:
    wide = Rect(0, 4, 10, 2)
    tall = Rect(4, 0, 2, 10)
    assert wide not in tall
    assert tall not in wide


@pytest.mark.parametrize(
    "a,b",
    [
        (Rect(0, 0, 10, 10), Rect(5, 5, 10, 10)),
        (Rect(0, 0, 10, 10), Rect(2, 2, 3, 3)),
        (Rect(2, 2, 3, 3), Rect(0, 0, 10, 10)),
        (Rect(0, 0, 10, 10), Rect(0, 0, 10, 10)),
        (Rect(0, 4, 10, 2), Rect(4, 0, 2, 10)),
        (Rect(0, 0, 10, 10), Rect(-5, -5, 7, 7)),
    ],
)
def test_rect_intersects(a: Rect, b: Rect) -> None:
    assert a.intersects(b)
    assert b.intersects(a)


@pytest.mark.parametrize(
    "a,b",
    [
        (Rect(0, 0, 1, 1), Rect(10, 10, 1, 1)),
        (Rect(0, 0, 1, 1), Rect(1, 0, 1, 1)),
        (Rect(0, 0, 1, 1), Rect(1, 1, 1, 1)),
        (Rect(0, 0, 1, 1), Rect(0, -1, 1, 1)),
    ],
)
def test_rect_does_not_intersect(a: Rect, b: Rect) -> None:
    assert not a.intersects(b)
    assert not b.intersects(a)


def test_rect_intersects_negative_dimensions() -> None:
    assert Rect(10, 10, -10, -10).intersects(Rect(5, 5, 10, 10))


def test_rect_intersects_invalid_type() -> None:
    with pytest.raises(TypeError):
        Rect().intersects("foo")


def test_rect_corner_a_is_a_copy() -> None:
    r = Rect(1, 2, 3, 4)
    r.A.x = 99
    assert r.x == 1
