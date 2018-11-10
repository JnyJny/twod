import pytest

from twod import Point, ColinearPoints


def test_point_invert_origin():
    p = Point()
    q = ~p
    r = ~q
    assert q.x == -1 and q.y == -1
    assert r == p and r is not p


def test_point_invert_positive():
    p = Point(2, 2)
    q = ~p
    r = ~q
    assert q.x == -3 and q.y == -3
    assert r == p and r is not p


def test_point_invert_negative():
    p = Point(-2, -2)
    q = ~p
    r = ~q
    assert q.x == 1 and q.y == 1
    assert r == p and r is not p


def test_point_invert_posneg():
    p = Point(-2, 2)
    q = ~p
    r = ~q
    assert q.x == 1 and q.y == -3
    assert r == p and r is not p


def test_point_invert_negpos():
    p = Point(2, -2)
    q = ~p
    r = ~q
    assert q.x == -3 and q.y == 1
    assert r == p and r is not p


def test_point_distance_to_self():
    p = Point()
    assert p.distance() == 0


def test_point_distance_reflexive():

    p = Point()
    q = Point(1, 1)
    assert p.distance(q) == q.distance(p)


def test_point_distance():
    p = Point()
    q = Point(2, 0)
    assert p.distance(q) == 2


def test_point_distance_squared_to_self():
    p = Point()
    assert p.distance_squared(p) == 0


def test_point_distance_squared_to_other():
    p = Point()
    q = Point(2, 0)
    assert p.distance_squared(q) == 4


def test_point_dot_origin():
    p = Point()
    q = Point()
    r = p.dot(q)
    assert r == 0


def test_point_dot_nonzero():
    p = Point(1, 2)
    q = Point(3, 4)
    r = p.dot(q)
    assert r == 11


def test_point_cross_origin():
    p = Point()
    q = Point()
    r = p.cross(q)
    assert r == 0

def test_point_cross_nonzero():
    p = Point(7, 2)
    q = Point(4, 3)
    r = p.cross(q)
    assert r == 29

def test_point_ccw_greater_than_zero():
    p = Point()
    q = Point(1, 0)
    r = Point(1, 1)
    assert p.ccw(q, r) > 0


def test_point_ccw_less_than_zero():
    p = Point()
    q = Point(1, 0)
    r = Point(1, 1)
    assert r.ccw(q, p) < 0


def test_point_ccw_equal_zero():
    p = Point()
    q = Point(1, 0)
    r = Point(2, 0)
    assert p.ccw(q, r) == 0


def test_point_is_ccw_true():
    p = Point()
    q = Point(1, 0)
    r = Point(1, 1)
    assert p.is_ccw(q, r)


def test_point_is_ccw_false():
    p = Point()
    q = Point(1, 0)
    r = Point(1, 1)
    assert not r.is_ccw(q, p)


def test_point_is_ccw_colinear():
    p = Point()
    q = Point(1, 0)
    r = Point(2, 0)
    with pytest.raises(ColinearPoints):
        p.is_ccw(q, r)


def test_point_midpoint_from_origin():
    p = Point(1, 1)
    o = Point()
    r = p.midpoint()
    s = o.midpoint(p)
    assert r.x == 0.5 and r.y == 0.5
    assert s == r


def test_point_midpoint_from_point():
    p = Point(1, 1)
    q = Point(2, 2)
    r = p.midpoint(q)
    s = q.midpoint(p)
    assert r.x == 1.5 and r.y == 1.5
    assert r == s


def test_point_between_x_true():
    a = Point()
    b = Point(2, 0)
    p = Point(1, 0)
    assert p.between(a, b)


def test_point_between_x_false():
    a = Point()
    b = Point(2, 0)
    p = Point(1, 0)
    assert not a.between(p, b)


def test_point_between_y_true():
    a = Point()
    b = Point(0, 2)
    p = Point(0, 1)
    assert p.between(a, b)


def test_point_between_y_false():
    a = Point()
    b = Point(0, 2)
    p = Point(0, 1)
    assert not a.between(p, b)


def test_point_between_true():
    a = Point()
    b = Point(2, 2)
    p = Point(1, 1)
    assert p.between(a, b)


def test_point_between_false():
    a = Point()
    b = Point(2, 2)
    p = Point(1, 1)
    assert not a.between(p, b)


def test_point_inside_true():
    a = Point()
    b = Point(2, 2)
    p = Point(1, 1)
    assert p.inside(a, b)


def test_point_inside_x_false():
    a = Point()
    b = Point(2, 2)
    p = Point(0, 1)
    r = Point(2, 1)
    assert not p.inside(a, b) and not r.inside(a, b)


def test_point_inside_y_false():
    a = Point()
    b = Point(2, 2)
    p = Point(1, 0)
    r = Point(1, 2)
    assert not p.inside(a, b) and not r.inside(a, b)


def test_point_inside_false():
    a = Point()
    b = Point(2, 2)
    p = Point(1, 1)
    assert not a.inside(p, b)


def test_point_abs_origin():
    o = Point()
    p = abs(o)
    assert p.x == 0 and p.y == 0


def test_point_abs_positive():
    p = Point(2, 3)
    q = abs(p)
    assert q.x == 2 and q.y == 3


def test_point_abs_mixed_sign():
    p = Point(-1, 1)
    q = Point(1, -1)
    r = abs(p)
    s = abs(q)
    assert r.x == 1 and r.y == 1
    assert s.x == 1 and s.y == 1


def test_point_abs_negative():
    p = Point(-1, -2)
    q = abs(p)
    assert q.x == 1 and q.y == 2


def test_point_neg_origin():
    o = Point()
    p = -o
    assert p.x == 0 and p.y == 0


def test_point_neg_positive():
    p = Point(2, 3)
    q = -p
    assert q.x == -2 and q.y == -3


def test_point_neg_mixed_sign():
    p = Point(-1, 1)
    q = Point(1, -1)
    r = -p
    s = -q
    assert r.x == 1 and r.y == -1
    assert s.x == -1 and s.y == 1


def test_point_neg_negative():
    p = Point(-1, -2)
    q = -p
    assert q.x == 1 and q.y == 2


def test_point_is_colinear_x_true():
    a = Point()
    b = Point(x=1)
    c = Point(x=2)
    assert a.is_colinear(b, c)


def test_point_is_colinear_x_false():
    a = Point()
    b = Point(y=1)
    c = Point(x=2)
    assert not a.is_colinear(b, c)


def test_point_is_colinear_y_true():
    a = Point()
    b = Point(y=1)
    c = Point(y=2)
    assert a.is_colinear(b, c)


def test_point_is_colinear_y_false():
    a = Point()
    b = Point(x=1)
    c = Point(y=2)
    assert not a.is_colinear(b, c)


def test_point_is_colinear_xy_true():
    a = Point()
    b = Point(1, 1)
    c = Point(2, 2)
    assert a.is_colinear(b, c)


def test_point_is_colinear_xy_false():
    a = Point()
    b = Point(1, 2)
    c = Point(3, 3)
    assert not a.is_colinear(b, c)
