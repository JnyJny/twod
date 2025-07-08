import pytest
from twod import CPoint as Point


@pytest.mark.skip()
def test_point_origin_pow():
    p = Point()
    q = p**2
    assert p == q


@pytest.mark.skip()
def test_point_origin_inplace_pow():
    p = Point()
    p **= 2
    assert p.x == 0 and p.y == 0


@pytest.mark.skip()
def test_point_nonzero_pow():
    p = Point(2, 4)
    q = p**2
    assert q.x == -12 and q.y == 16


@pytest.mark.skip()
def test_point_nonzero_inplace_pow():
    p = Point(2, 4)
    p **= 2
    assert p.x == -12 and p.y == 16
