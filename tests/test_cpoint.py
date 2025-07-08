import pytest
from twod import CPoint, Quadrant


def test_cpoint_creation_without_args():
    p = CPoint()
    assert p.x == 0 and p.y == 0
    assert p.is_origin
    assert p.polar == (0, 0)
    assert p.quadrant == Quadrant.ORIGIN


def test_cpoint_creation_with_x_arg():
    p = CPoint(1)
    assert p.x == 1 and p.y == 0
    q = CPoint(x=2)
    assert q.x == 2 and q.y == 0


def test_cpoint_creation_with_y_arg():
    p = CPoint(y=1)
    assert p.x == 0 and p.y == 1


def test_cpoint_create_with_two_args():
    p = CPoint(1, 2)
    assert p.x == 1 and p.y == 2
    assert not p.is_origin


def test_cpoint_equality():
    p = CPoint(1, 1)
    r = CPoint(1, 1)
    assert p == r and p is not r


def test_cpoint_inequality():
    p = CPoint()
    r = CPoint(1, 1)
    assert p != r and p is not r


@pytest.mark.parametrize(
    "x,y,expected",
    [
        (0, 0, Quadrant.ORIGIN),
        (1, 1, Quadrant.FIRST),
        (-1, 1, Quadrant.SECOND),
        (-1, -1, Quadrant.THIRD),
        (1, -1, Quadrant.FOURTH),
        (0, 1, Quadrant.Y_AXIS),
        (1, 0, Quadrant.X_AXIS),
    ],
)
def test_cpoint_quadrant_location(x, y, expected) -> None:
    assert CPoint(x, y).quadrant == expected


def test_cpoint_xy_property():

    p = CPoint(4, 5)

    assert p.xy == (4, 5)

    p.xy = (2, 3)

    assert p.x == 2 and p.y == 3

    with pytest.raises(TypeError):
        p.xy = "nonsense"

    with pytest.raises(TypeError):
        p.xy = 1


def test_cpoint_getitem_int_key():

    p = CPoint(1, 2)

    assert p[0] == 1
    assert p[1] == 2

    with pytest.raises(IndexError):
        p[2]


@pytest.mark.parametrize(
    "A, key, expected",
    [
        [(1, 2), slice(0, 1), 1],
        [(1, 2), slice(1, 2), 2],
    ],
)
def test_cpoint_getitem_slice_key(A, key, expected):
    p = CPoint(*A)
    assert p[key] == expected


@pytest.mark.parametrize("key", [0.0, "foo", {}])
def test_cpoint_getitem_invalid_key(key, point):
    with pytest.raises(TypeError):
        point[key]


def test_cpoint_setitem_valid_key(point):

    assert point == (0, 0)
    point[0] = 1
    point[1] = 2
    assert point == (1, 2)


@pytest.mark.parametrize("key", range(-16, 16, 3))
def test_cpoint_setitem_key_out_of_range(key, point):
    with pytest.raises(IndexError):
        point[key] = 0


@pytest.mark.parametrize("key", [0.0, "foo", {}])
def test_cpoint_setitem_invalid_key(key, point):
    with pytest.raises(TypeError):
        point[key] = 0
