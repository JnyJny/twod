
import pytest

from twod import Point, ColinearPoints

def test_point_creation_without_args():
    p = Point()
    assert p.x == 0 and p.y == 0
    assert p.is_origin

def test_point_create_with_args():
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
    assert r.x == .5 and r.y == .5
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
    assert p.between(a,b)

def test_point_between_x_false():
    a = Point()
    b = Point(2, 0)
    p = Point(1, 0)
    assert not a.between(p, b)

def test_point_between_y_true():
    a = Point()
    b = Point(0, 2)
    p = Point(0, 1)
    assert p.between(a,b)

def test_point_between_y_false():
    a = Point()
    b = Point(0, 2)
    p = Point(0, 1)
    assert not a.between(p, b)    

def test_point_between_true():
    a = Point()
    b = Point(2, 2)
    p = Point(1, 1)
    assert p.between(a,b)

def test_point_between_false():
    a = Point()
    b = Point(2, 2)
    p = Point(1, 1)
    assert not a.between(p, b)    
