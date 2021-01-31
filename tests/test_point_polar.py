"""
"""

import pytest
import math

from twod import Point


def test_point_from_polar_origin_radians():
    p = Point.from_polar(0, 0)
    assert p.is_origin


def test_point_from_polar_origin_degrees():
    p = Point.from_polar(0, 0, is_radians=False)
    assert p.is_origin


@pytest.mark.parametrize(
    "to",
    [
        Point(1, 1),
        (1, 1),
        [1, 1],
    ],
)
def test_point_from_polar_translate(to):
    p = Point.from_polar(0, 0, translate=to)
    assert p == to


@pytest.mark.parametrize("x, y", [(1, 1), (-1, 1), (-1, -1), (1, -1)])
def test_point_from_polar_not_origin_all_quadrants(x, y):

    radius = math.hypot(x, y)
    radians = math.atan2(y, x)
    degrees = math.degrees(radians)

    p = Point.from_polar(radius, radians)
    q = Point.from_polar(radius, degrees, is_radians=False)

    i = Point()
    i.radius = radius
    i.radians = radians

    j = Point()
    j.radius = radius
    j.degrees = degrees

    assert p.x == x and p.y == y
    assert q.x == x and q.y == y
    assert i.x == x and i.y == y
    assert j.x == x and j.y == y
    assert p == q == i == j


def test_point_polar_assignment():
    p = Point()
    q = Point(1, 1)
    assert p.polar != q.polar and p != q and p is not q
    p.polar = q.polar
    assert p == q

    with pytest.raises(TypeError):
        p.polar = 1

    with pytest.raises(TypeError):
        p.polar = "foobar"


def test_point_polar_deg_assignment():
    p = Point()
    q = Point(1, 1)
    assert p.polar_deg != q.polar_deg and p != q and p is not q
    p.polar_deg = q.polar_deg
    assert p == q

    with pytest.raises(TypeError):
        p.polar_deg = 1

    with pytest.raises(TypeError):
        p.polar_deg = "ackqux"


def test_point_polar_calculation():
    assert Point().polar_deg[1] == 0
    assert Point(1, 0).polar_deg[0] == 1
    assert Point(0, 1).polar_deg[0] == 1
    assert Point(-1, 0).polar_deg[0] == 1
    assert Point(0, -1).polar_deg[0] == 1
    assert Point(1, 0).polar_deg[1] == 0
    assert Point(0, 1).polar_deg[1] == 90
    assert Point(-1, 0).polar_deg[1] == 180
    assert Point(0, -1).polar_deg[1] == -90
    d = math.hypot(1, 1)
    assert Point(1, 1).polar_deg[0] == d
    assert Point(-1, 1).polar_deg[0] == d
    assert Point(-1, -1).polar_deg[0] == d
    assert Point(1, -1).polar_deg[0] == d
    assert Point(1, 1).polar_deg[1] == 45
    assert Point(-1, 1).polar_deg[1] == 135
    assert Point(-1, -1).polar_deg[1] == -135
    assert Point(1, -1).polar_deg[1] == -45


def test_point_radius_property():
    p = Point(1, 1)
    r = math.hypot(1, 1)
    assert p.radius == r

    p.radius *= 3
    # XXX epsilons are biting me here.
    assert round(p.radius, 13) == round(3 * r, 13)

    p.radius = 0
    assert p.radius == 0 and p.is_origin


def test_point_radians_degrees_properties():
    p = Point(1, 1)
    r = math.atan2(1, 1)
    d = math.degrees(r)
    assert p.radians == r
    assert p.degrees == d
