""" """

import pytest
from twod import CPoint as Point
from twod import CRect as Rect

# EJO Needs more literal edge case testing where points are on the
#     edges of a rectangle.


def test_point_in_crect() -> None:
    p = Point(1, 1)
    bb = Rect(0, 0, 2, 2)
    assert p in bb


def test_point_not_in_crect() -> None:
    p = Point()
    bb = Rect(1, 1, 2, 2)
    assert p not in bb


def test_embedded_rect_in_crect() -> None:
    bb = Rect(1, 1, 1, 1)
    qq = Rect(0, 0, 3, 3)
    assert bb in qq
    assert qq not in bb


def test_rect_not_in_crect() -> None:
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
def test_crect_adjacent_to_crect(a: Rect, b: Rect) -> None:
    assert a not in b
    assert b not in a


def test_same_crect_inside() -> None:
    r = Rect(0, 0, 1, 1)
    assert r not in r
