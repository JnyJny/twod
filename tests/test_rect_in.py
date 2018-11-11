from twod import Point, Rect


def test_point_in_rect():
    bb = Rect(1, 1, 2, 2)
    assert bb.center in bb


def test_point_not_in_rect():
    p = Point()
    bb = Rect(1, 1, 2, 2)
    assert p not in bb


def test_rect_in_rect():
    bb = Rect(1, 1, 1, 1)
    qq = Rect(0, 0, 3, 3)
    assert bb in qq


def test_outer_rect_in_inner_rect():
    bb = Rect(1, 1, 1, 1)
    qq = Rect(0, 0, 3, 3)
    assert qq in bb


def test_rect_not_in_rect():
    bb = Rect(0, 0, 1, 1)
    qq = Rect(10, 10, 1, 1)
    assert bb not in qq
    assert qq not in bb
