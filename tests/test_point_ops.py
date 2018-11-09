
from twod import Point

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

    
    
