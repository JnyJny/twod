from twod import Point


def test_point_origin_pow():
    p = Point()
    q = p ** 2
    assert p == q


def test_point_origin_inplace_pow():
    p = Point()
    p **= 2
    assert p.x == 0 and p.y == 0


def test_point_nonzero_pow():
    p = Point(2, 4)
    q = p ** 2
    assert q.x == 4 and q.y == 16


def test_point_nonzero_inplace_pow():
    p = Point(2, 4)
    p **= 2
    assert p.x == 4 and p.y == 16
