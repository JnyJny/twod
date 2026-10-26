"""test the Point-like contract: a Point or a Sequence of two numbers"""

from collections import deque
from collections.abc import Sequence

import pytest
from twod import Circle, Ellipse, Point, Rect


class Pair(Sequence):
    """A minimal Sequence that is neither a list nor a tuple."""

    def __init__(self, x, y):
        self._v = (x, y)

    def __len__(self):
        return 2

    def __getitem__(self, index):
        return self._v[index]


ACCEPTED = [
    pytest.param((3, 4), id="tuple"),
    pytest.param([3, 4], id="list"),
    pytest.param(range(3, 5), id="range"),
    pytest.param(deque([3, 4]), id="deque"),
    pytest.param(Pair(3, 4), id="custom-sequence"),
    pytest.param(Point(3, 4), id="point"),
]

REJECTED = [
    pytest.param("34", id="str"),
    pytest.param(b"\x03\x04", id="bytes"),
    pytest.param(bytearray(b"\x03\x04"), id="bytearray"),
    pytest.param({3, 4}, id="set"),
    pytest.param(frozenset({3, 4}), id="frozenset"),
    pytest.param({"x": 3, "y": 4}, id="dict"),
    pytest.param(3 + 4j, id="complex"),
    pytest.param(iter((3, 4)), id="iterator"),
    pytest.param((n for n in (3, 4)), id="generator"),
    pytest.param(None, id="none"),
    pytest.param(3, id="scalar"),
]


@pytest.mark.parametrize("value", ACCEPTED)
def test_from_point_like_accepts(value):
    assert Point.from_point_like(value) == Point(3, 4)


@pytest.mark.parametrize("value", REJECTED)
def test_from_point_like_rejects(value):
    with pytest.raises(TypeError):
        Point.from_point_like(value)


def test_from_point_like_returns_a_point_as_is():
    p = Point(1, 2)
    assert Point.from_point_like(p) is p


@pytest.mark.parametrize("value", ACCEPTED)
def test_geometry_methods_accept(value):
    assert Point().distance(value) == 5
    assert Point().distance_squared(value) == 25
    assert Point(1, 0).dot(value) == 3
    assert Point(1, 0).cross(value) == 4
    assert Point(0, 0).midpoint(value) == Point(1.5, 2)
    assert Point(3, 4).between(value, value)
    assert Point().ccw(value, (0, 1)) != 0
    assert Point().rotate(0, origin=value, inplace=False) == Point()


@pytest.mark.parametrize("value", REJECTED)
def test_geometry_methods_reject(value):
    if value is not None:  # distance(None) means the origin
        with pytest.raises(TypeError):
            Point().distance(value)
    with pytest.raises(TypeError):
        Point().dot(value)
    with pytest.raises(TypeError):
        Point().between(value, (0, 0))


@pytest.mark.parametrize("value", ACCEPTED)
def test_point_operators_accept(value):
    p = Point(1, 1)
    assert p + value == Point(4, 5)
    assert p - value == Point(-2, -3)
    assert p * value == Point(3, 4)
    assert p / value == Point(1 / 3, 1 / 4)
    assert p // value == Point(0, 0)
    q = Point(1, 1)
    q += value
    assert q == Point(4, 5)


@pytest.mark.parametrize(
    "value", [v for v in REJECTED if v.id not in ("scalar", "none")]
)
def test_point_operators_reject(value):
    p = Point(1, 1)
    with pytest.raises(TypeError):
        p + value
    with pytest.raises(TypeError):
        p += value


def test_point_operators_still_accept_scalars():
    assert Point(1, 2) + 1 == Point(2, 3)
    assert Point(1, 2) * 2 == Point(2, 4)


def test_point_operator_error_leaves_point_unchanged():
    p = Point(1, 1)
    with pytest.raises(ZeroDivisionError):
        p /= (1, 0)
    assert p == Point(1, 1)


@pytest.mark.parametrize("value", ACCEPTED)
def test_point_setters_accept(value):
    p = Point()
    p.xy = value
    assert p.xy == (3, 4)
    p.polar = value
    assert p.xy == pytest.approx(Point.from_polar(3, 4).xy)
    p.polar_deg = value
    assert p.xy == pytest.approx(Point.from_polar(3, 4, is_radians=False).xy)


@pytest.mark.parametrize("value", REJECTED)
def test_point_setters_reject(value):
    p = Point(1, 2)
    with pytest.raises(TypeError):
        p.xy = value
    with pytest.raises(TypeError):
        p.polar = value
    with pytest.raises(TypeError):
        p.polar_deg = value
    assert p.xy == (1, 2)


@pytest.mark.parametrize("value", ACCEPTED)
def test_rect_accepts(value):
    r = Rect(0, 0, 10, 10)
    assert r + value == Rect(3, 4, 10, 10)
    assert value in r
    r.xy = value
    r.wh = value
    assert (r.x, r.y, r.w, r.h) == (3, 4, 3, 4)


@pytest.mark.parametrize(
    "value", [v for v in REJECTED if v.id not in ("scalar", "none")]
)
def test_rect_rejects(value):
    r = Rect(0, 0, 10, 10)
    with pytest.raises(TypeError):
        r + value
    with pytest.raises(TypeError):
        value in r


# Each factory builds the pair (x, x + 1) as a different kind of Point-like.
FACTORIES = [
    pytest.param(lambda x: (x, x + 1), id="tuple"),
    pytest.param(lambda x: [x, x + 1], id="list"),
    pytest.param(lambda x: range(x, x + 2), id="range"),
    pytest.param(lambda x: deque([x, x + 1]), id="deque"),
    pytest.param(lambda x: Pair(x, x + 1), id="custom-sequence"),
    pytest.param(lambda x: Point(x, x + 1), id="point"),
]


@pytest.mark.parametrize("shape", [Circle(0, 0, 5), Ellipse(0, 0, 3, 5)])
@pytest.mark.parametrize("make", FACTORIES)
def test_shape_containment_accepts(shape, make):
    assert make(1) in shape
    assert make(9) not in shape


@pytest.mark.parametrize("shape", [Circle(0, 0, 5), Ellipse(0, 0, 3, 5)])
@pytest.mark.parametrize("value", REJECTED)
def test_shape_containment_rejects(shape, value):
    with pytest.raises(TypeError):
        value in shape


@pytest.mark.parametrize("shape", [Circle(), Ellipse()])
@pytest.mark.parametrize("value", ACCEPTED)
def test_shape_position_accepts(shape, value):
    shape.xy = value
    shape.center = value
    assert shape.xy == (3, 4)


@pytest.mark.parametrize("shape", [Circle(), Ellipse()])
@pytest.mark.parametrize("value", REJECTED)
def test_shape_position_rejects(shape, value):
    with pytest.raises(TypeError):
        shape.center = value
