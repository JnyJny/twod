import pytest

from twod import CPoint as Point
from twod import CRect as Rect


def test_rect_floordiv_empty():
    r = Rect()
    s = Rect()
    with pytest.raises(ZeroDivisionError):
        _ = r // s


def test_rect_floordiv_xy():
    r = Rect(1, 2)
    s = Rect(3, 4)
    with pytest.raises(ZeroDivisionError):
        _ = r // s


def test_rect_floordiv_wh():
    r = Rect(w=1, h=2)
    s = Rect(w=3, h=4)
    with pytest.raises(ZeroDivisionError):
        _ = r // s


def test_rect_floordiv_xywh():
    r = Rect(2, 4, 6, 8)
    s = Rect(2, 2, 2, 2)
    q = r // s
    assert q.x == 1 and q.y == 2 and q.w == 3 and q.h == 4


def test_rect_floordiv_empty_point():
    p = Point()
    r = Rect(1, 2, 3, 4)
    with pytest.raises(ZeroDivisionError):
        _ = r // p


def test_rect_floordiv_nonempty_point():
    r = Rect(2, 4, 6, 8)
    p = Point(2, 2)
    q = r // p
    assert q.x == 1 and q.y == 2 and q.w == 6 and q.h == 8


def test_rect_ifloordiv_empty_point():
    r = Rect(1, 2, 3, 4)
    p = Point()
    with pytest.raises(ZeroDivisionError):
        r //= p


def test_rect_ifloordiv_nonempty_point():
    r = Rect(2, 4, 6, 8)
    p = Point(2, 2)
    r //= p
    assert r.x == 1 and r.y == 2 and r.w == 6 and r.h == 8


def test_rect_ifloordiv_empty_rect():
    r = Rect(1, 2, 3, 4)
    s = Rect()
    with pytest.raises(ZeroDivisionError):
        r //= s


def test_rect_ifloordiv_nonempty_rect():
    r = Rect(2, 4, 6, 8)
    s = Rect(2, 2, 2, 2)
    r //= s
    assert r.x == 1 and r.y == 2 and r.w == 3 and r.h == 4
