from twod import Point, Rect


def test_rect_mul_empty():
    r = Rect()
    s = Rect()
    q = r * s
    assert q.x == 0 and q.y == 0 and q.w == 0 and q.h == 0
    assert q == r and q == s and q is not r and q is not s


def test_rect_mul_xy():
    r = Rect(1, 2)
    s = Rect(3, 4)
    q = r * s
    assert q.x == 3 and q.y == 8 and q.w == 0 and q.h == 0


def test_rect_mul_wh():
    r = Rect(w=1, h=2)
    s = Rect(w=3, h=4)
    q = r * s
    assert q.x == 0 and q.y == 0 and q.w == 3 and q.h == 8


def test_rect_mul_xywh():
    r = Rect(1, 2, 3, 4)
    s = Rect(5, 6, 7, 8)
    q = r * s
    assert q.x == 5 and q.y == 12 and q.w == 21 and q.h == 32


def test_rect_mul_empty_point():
    p = Point()
    r = Rect(1, 2, 3, 4)
    q = r * p
    assert q.x == 0 and q.y == 0 and q.w == 3 and q.h == 4


def test_rect_mul_nonempty_point():
    r = Rect(1, 2, 3, 4)
    p = Point(2, 3)
    q = r * p
    assert q.x == 2 and q.y == 6 and q.w == 3 and q.h == 4


def test_rect_imul_empty_point():
    r = Rect(1, 2, 3, 4)
    p = Point()
    r *= p
    assert r.x == 0 and r.y == 0 and r.w == 3 and r.h == 4


def test_rect_imul_nonempty_point():
    r = Rect(1, 2, 3, 4)
    p = Point(1, 2)
    r *= p
    assert r.x == 1 and r.y == 4 and r.w == 3 and r.h == 4


def test_rect_imul_empty_rect():
    r = Rect(1, 2, 3, 4)
    s = Rect()
    r *= s
    assert r.x == 0 and r.y == 0 and r.w == 0 and r.h == 0
