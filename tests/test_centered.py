"""Tests for the Centered mixin"""

import pytest
from twod import Centered, Circle, Ellipse, Point


class Disc(Centered):
    def __init__(self, x=0, y=0):
        self._p = Point(x, y)


def test_centered_exported_from_package():
    import twod.centered

    assert Centered is twod.centered.Centered


def test_centered_properties():
    d = Disc(1, 2)
    assert (d.x, d.y, d.xy) == (1, 2, (1, 2))
    d.x = 3
    d.y = 4
    assert d.xy == (3, 4)
    d.xy = [5, 6]
    assert d.center == Point(5, 6)
    d.center = (7, 8)
    assert d.xy == (7, 8)


def test_centered_center_is_a_copy():
    d = Disc(1, 2)
    d.center.x = 99
    assert d.x == 1


@pytest.mark.parametrize("bad", ["foo", None, 5])
def test_centered_rejects_unconvertible_position(bad):
    with pytest.raises(TypeError):
        Disc().center = bad


def test_centered_adds_no_point_methods():
    d = Disc()
    assert not isinstance(d, Point)
    assert not hasattr(d, "polar")
    assert not hasattr(d, "distance")


@pytest.mark.parametrize("shape", [Circle(), Ellipse()])
def test_shapes_use_centered(shape):
    assert isinstance(shape, Centered)
