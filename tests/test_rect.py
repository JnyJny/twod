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
