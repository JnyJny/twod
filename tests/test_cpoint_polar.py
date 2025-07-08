""" """

import cmath
import math

import pytest
from twod import CPoint as Point


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


@pytest.mark.parametrize(
    "x, y",
    [
        (1, 1),
        (-1, 1),
        (-1, -1),
        (1, -1),
    ],
)
def test_point_from_polar_not_origin_all_quadrants(x, y):

    radius, radians = cmath.polar(complex(x, y))
    degrees = math.degrees(radians)

    p = Point.from_polar(radius, radians)
    q = Point.from_polar(radius, degrees, is_radians=False)

    i = Point()
    i.radius = radius
    i.radians = radians

    j = Point()
    j.radius = radius
    j.degrees = degrees

    assert cmath.isclose(p.x, x)
    assert cmath.isclose(p.y, y)
    assert cmath.isclose(q.x, x)
    assert cmath.isclose(q.y, y)
    assert cmath.isclose(i.x, x)
    assert cmath.isclose(i.y, y)
    assert cmath.isclose(j.x, x)
    assert cmath.isclose(j.y, y)
    assert p == q == i == j


@pytest.mark.skip()
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


@pytest.mark.skip()
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
    assert Point().degrees == 0
    assert Point(1, 0).radius == 1
    assert Point(0, 1).radius == 1
    assert Point(-1, 0).radius == 1
    assert Point(0, -1).radius == 1
    assert Point(1, 0).degrees == 0
    assert Point(0, 1).degrees == 90
    assert Point(-1, 0).degrees == 180
    assert Point(0, -1).degrees == -90
    d = math.hypot(1, 1)
    assert Point(1, 1).radius == d
    assert Point(-1, 1).radius == d
    assert Point(-1, -1).radius == d
    assert Point(1, -1).radius == d
    assert Point(1, 1).degrees == 45
    assert Point(-1, 1).degrees == 135
    assert Point(-1, -1).degrees == -135
    assert Point(1, -1).degrees == -45


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
