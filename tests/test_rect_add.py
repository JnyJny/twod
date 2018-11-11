from twod import Point, Rect


def test_rect_add_empty():
    r = Rect()
    s = Rect()
    q = r + s
    assert q.x == 0 and q.y == 0 and q.w == 0 and q.h == 0
    assert q == r and q == s and q is not r and q is not s


def test_rect_add_xy():
    r = Rect(1, 2)
    s = Rect(3, 4)
    q = r + s
    assert q.x == 4 and q.y == 6 and q.w == 0 and q.h == 0


def test_rect_add_wh():
    r = Rect(w=1, h=2)
    s = Rect(w=3, h=4)
    q = r + s
    assert q.x == 0 and q.y == 0 and q.w == 4 and q.h == 6


def test_rect_add_xywh():
    r = Rect(1, 2, 3, 4)
    s = Rect(5, 6, 7, 8)
    q = r + s
    assert q.x == 6 and q.y == 8 and q.w == 10 and q.h == 12


def test_rect_add_empty_point():
    p = Point()
    r = Rect(1, 2, 3, 4)
    q = r + p
    assert q.x == 1 and q.y == 2 and q.w == 3 and q.h == 4


def test_rect_add_nonempty_point():
    r = Rect(1, 2, 3, 4)
    p = Point(2, 3)
    q = r + p
    assert q.x == 3 and q.y == 5 and q.w == 3 and q.h == 4


def test_rect_iadd_empty_point():
    r = Rect(1, 2, 3, 4)
    p = Point()
    r += p
    assert r.x == 1 and r.y == 2 and r.w == 3 and r.h == 4


def test_rect_iadd_nonempty_point():

    r = Rect(1, 2, 3, 4)
    p = Point(1, 2)
    r += p
    assert r.x == 2 and r.y == 4 and r.w == 3 and r.h == 4


def test_rect_iadd_empty_rect():
    r = Rect(1, 2, 3, 4)
    s = Rect()
    r += s
    assert r.x == 1 and r.y == 2 and r.w == 3 and r.h == 4
