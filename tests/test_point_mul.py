from twod import Point


def test_point_multiplication_with_zero_points():
    p = Point()
    q = Point()
    r = p * q
    assert r.x == 0 and r.y == 0


def test_point_multiplication_with_nonzero_points():
    p = Point()
    q = Point(1, 1)
    r = p * q
    assert r.x == 0 and r.y == 0


def test_point_multiplication_with_scalars():
    p = Point() * 1
    assert p.x == 0 and p.y == 0


def test_point_inplace_multiplication_with_zero_points():
    p = Point()
    p *= Point()
    assert p.x == 0 and p.y == 0


def test_point_inplace_multiplication_with_nonzero_points():
    p = Point(1, 2)
    p *= Point(2, 3)
    assert p.x == 2 and p.y == 6


def test_point_inplace_multiplication_with_scalars():

    p = Point(1, 2)
    p *= 2
    assert p.x == 2 and p.y == 4
