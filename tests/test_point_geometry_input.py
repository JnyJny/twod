"""test Point geometry methods accepting tuples and lists like a human™"""

import math

import pytest
from twod import ColinearPoints, Point


@pytest.mark.parametrize("other", [(3, 4), [3, 4], Point(3, 4)])
def test_point_distance_accepts_point_like(other):
    assert Point().distance(other) == 5


def test_point_distance_is_exact_for_integers():
    assert Point(1, 1).distance_squared((4, 5)) == 25
    assert isinstance(Point(1, 1).distance_squared((4, 5)), int)


def test_point_distance_does_not_overflow_large_values():
    assert math.isclose(Point(1e200, 1e200).distance(), math.sqrt(2) * 1e200)


@pytest.mark.parametrize("other", [(3, 4), [3, 4], Point(3, 4)])
def test_point_dot_cross_accept_point_like(other):
    p = Point(1, 2)
    assert p.dot(other) == 11
    assert p.cross(other) == -2


@pytest.mark.parametrize("b,c", [((1, 0), (0, 1)), ([1, 0], [0, 1])])
def test_point_winding_accepts_point_like(b, c):
    p = Point()
    assert p.ccw(b, c) > 0
    assert p.is_ccw(b, c)
    assert not p.is_colinear(b, c)


def test_point_is_ccw_colinear_point_like():
    with pytest.raises(ColinearPoints):
        Point().is_ccw((1, 1), (2, 2))


def test_point_midpoint_accepts_point_like():
    assert Point(0, 0).midpoint((2, 4)) == Point(1, 2)
    assert Point(2, 4).midpoint() == Point(1, 2)


def test_point_between_inside_accept_point_like():
    p = Point(1, 1)
    assert p.between((0, 0), (1, 1))
    assert not p.inside((0, 0), (1, 1))
    assert p.inside([0, 0], [2, 2])


@pytest.mark.parametrize("bad", ["foo", object(), None])
def test_point_geometry_rejects_unconvertible(bad):
    with pytest.raises(TypeError):
        Point().dot(bad)


def test_point_rotate_quarter_turn_about_origin():
    p = Point(1, 0).rotate(90, is_degrees=True)
    assert p.xy == pytest.approx((0, 1))


def test_point_rotate_radians_about_other_point():
    p = Point(2, 1).rotate(math.pi, origin=(1, 1))
    assert p.xy == pytest.approx((0, 1))


def test_point_rotate_inplace_returns_self():
    p = Point(1, 0)
    q = p.rotate(math.pi / 2)
    assert q is p
    assert p.xy == pytest.approx((0, 1))


def test_point_rotate_not_inplace_leaves_original():
    p = Point(1, 0)
    q = p.rotate(math.pi / 2, inplace=False)
    assert q is not p
    assert p.xy == (1, 0)
    assert q.xy == pytest.approx((0, 1))


def test_point_rotate_preserves_distance_from_origin_point():
    p = Point(5, 7)
    q = p.rotate(1.234, origin=(2, 3), inplace=False)
    assert Point(2, 3).distance(q) == pytest.approx(Point(2, 3).distance(p))


def test_point_scale():
    p = Point(1, -2)
    assert p.scale(3) is p
    assert p.xy == (3, -6)
