""" """

import pytest
from twod import CPoint as Point
from twod import CRect as Rect


def test_crect_repr():
    """Test CRect string representation"""
    rect = Rect(1, 2, 3, 4)
    expected = "CRect(x=1.0, y=2.0, w=3.0, h=4.0)"
    assert repr(rect) == expected


def test_crect_equality_with_invalid_type():
    """Test CRect equality with invalid type returns NotImplemented"""
    rect = Rect(1, 2, 3, 4)
    result = rect.__eq__("not a rect")
    assert result is NotImplemented


def test_crect_contains_with_invalid_type():
    """Test CRect contains with invalid type returns NotImplemented"""
    rect = Rect(1, 2, 3, 4)
    result = rect.__contains__("not a point or rect")
    assert result is NotImplemented


def test_crect_edge_properties():
    """Test CRect edge properties AB, BC, CD, DA"""
    rect = Rect(1, 2, 3, 4)
    
    # Test AB edge (from A to B)
    ab = rect.AB
    assert ab == (rect.A, rect.B)
    assert ab[0] == Point(1, 2)
    assert ab[1] == Point(4, 2)
    
    # Test BC edge (from B to C)
    bc = rect.BC
    assert bc == (rect.B, rect.C)
    assert bc[0] == Point(4, 2)
    assert bc[1] == Point(4, 6)
    
    # Test CD edge (from C to D)
    cd = rect.CD
    assert cd == (rect.C, rect.D)
    assert cd[0] == Point(4, 6)
    assert cd[1] == Point(1, 6)
    
    # Test DA edge (from D to A)
    da = rect.DA
    assert da == (rect.D, rect.A)
    assert da[0] == Point(1, 6)
    assert da[1] == Point(1, 2)


def test_crect_ac_bd_diagonals():
    """Test CRect diagonal properties AC and BD"""
    rect = Rect(1, 2, 3, 4)
    
    # Test AC diagonal
    ac = rect.AC
    assert ac == (rect.A, rect.C)
    assert ac[0] == Point(1, 2)
    assert ac[1] == Point(4, 6)
    
    # Test BD diagonal
    bd = rect.BD
    assert bd == (rect.B, rect.D)
    assert bd[0] == Point(4, 2)
    assert bd[1] == Point(1, 6)


def test_crect_op_method_unsupported_type():
    """Test CRect _op method with unsupported type"""
    rect = Rect(1, 2, 3, 4)
    result = rect._op("invalid", lambda x, y: x + y)
    assert result is NotImplemented

A_RANGE = list(range(-10, 10))


def test_rect_creation_no_args() -> None:
    r = Rect()
    assert r.x == 0 and r.y == 0 and r.w == 0 and r.h == 0


@pytest.mark.parametrize("x", A_RANGE)
def test_rect_creation_x_args(x) -> None:
    r = Rect(x)
    q = Rect(x=x)
    assert r.x == x and r.y == 0 and r.w == 0 and r.h == 0
    assert q.x == x and q.y == 0 and q.w == 0 and q.h == 0


@pytest.mark.parametrize("y", A_RANGE)
def test_rect_creation_y_arg(y) -> None:
    r = Rect(y=y)
    assert r.x == 0 and r.y == y and r.w == 0 and r.h == 0


@pytest.mark.parametrize("x,y", list(zip(A_RANGE, A_RANGE)))
def test_rect_creation_xy_args(x, y) -> None:
    r = Rect(x, y)
    assert r.x == x and r.y == y and r.w == 0 and r.h == 0


@pytest.mark.parametrize("w,h", list(zip(A_RANGE, A_RANGE)))
def test_rect_creation_wh_args(w, h) -> None:
    r = Rect(w=w, h=h)
    assert r.x == 0 and r.y == 0 and r.w == w and r.h == h


@pytest.mark.parametrize("x,y,w,h", list(zip(A_RANGE, A_RANGE, A_RANGE, A_RANGE)))
def test_rect_creation_all_args(x, y, w, h) -> None:
    r = Rect(x, y, w, h)
    assert r.x == x and r.y == y and r.w == w and r.h == h


def test_rect_equality_empty() -> None:
    r = Rect()
    q = Rect()
    assert r == q
    assert r == r
    assert q == r
    assert q == q


@pytest.mark.parametrize("x,y,w,h", list(zip(A_RANGE, A_RANGE, A_RANGE, A_RANGE)))
def test_rect_equality_nonempty(x, y, w, h) -> None:
    r = Rect(x, y, w, h)
    q = Rect(x, y, w, h)
    assert r == q
    assert r == r
    assert q == r
    assert q == q


@pytest.mark.parametrize(
    "x,y,w,h, A, B, C, D",
    [
        (1, 2, 3, 4, (1, 2), (4, 2), (4, 6), (1, 6)),
    ],
)
def test_rect_vertex_properties(x, y, w, h, A, B, C, D) -> None:
    r = Rect(x, y, w, h)

    assert tuple(r.A) == A
    assert tuple(r.B) == B
    assert tuple(r.C) == C
    assert tuple(r.D) == D

    for vertex, value in zip(r.vertices, [A, B, C, D]):
        assert tuple(vertex) == value


def test_rect_sides() -> None:
    expected = [10, 5, 10, 5]

    assert Rect(w=10, h=5).sides == expected
    assert Rect(w=5, h=10).sides == expected[::-1]


@pytest.mark.parametrize(
    "x,y,w,h,expected",
    [
        (0, 0, 0, 0, 0),
        (0, 0, 1, 1, 4),
        (1, 2, 3, 4, 14),
    ],
)
def test_rect_perimeter(x, y, w, h, expected) -> None:
    assert Rect(x, y, w, h).perimeter == expected


@pytest.mark.parametrize(
    "x,y,w,h,expected",
    [
        (0, 0, 0, 0, 0),
        (0, 0, 1, 1, 1),
        (1, 2, 3, 4, 12),
    ],
)
def test_rect_area(x, y, w, h, expected) -> None:
    assert Rect(x, y, w, h).area == expected


@pytest.mark.parametrize(
    "x,y,w,h,expected",
    [
        (0, 0, 0, 0, Point()),
        (0, 0, 2, 2, Point(1, 1)),
        (1, 2, 3, 4, Point(2.5, 4)),
    ],
)
def test_rect_center_getter(x, y, w, h, expected):
    r = Rect(x, y, w, h)
    assert r.center == expected
    assert r.center == r.B.midpoint(r.D)


def test_rect_center_setter() -> None:

    r = Rect(0, 0, w=2, h=2)
    q = Rect(0, 0, w=2, h=2)

    assert r.center == q.center
    assert r.perimeter == q.perimeter
    assert r.area == q.area
    assert r.sides == q.sides

    new_center = (0, 0)

    r.center = new_center

    assert r.center != q.center and r.center == Point(*new_center)
    assert r.A == Point(-1, -1)
    assert r.B == Point(1, -1)
    assert r.C == Point(1, 1)
    assert r.D == Point(-1, 1)

    assert r.perimeter == q.perimeter
    assert r.area == q.area
    assert r.sides == q.sides
