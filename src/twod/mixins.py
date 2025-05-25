""" """

from typing import Any

from . import CPoint as Point


class MixinPoint:
    _p = Point()

    @property
    def x(self) -> float:
        return self._p.x

    @x.setter
    def x(self, new_x: float | int) -> None:
        self._p.x = new_x

    @property
    def y(self) -> float:
        return self._p.y

    @y.setter
    def y(self, new_y: float | int) -> None:
        self._p.y = new_y

    @property
    def xy(self) -> tuple[float, float]:
        return self._p.xy

    @xy.setter
    def xy(self, new_xy: Any) -> None:
        self._p.xy = new_xy


class MixinDimension:
    _d = Point()

    @property
    def w(self) -> float:
        return self._d.x

    @w.setter
    def w(self, new_w: float | int) -> None:
        self._d.x = new_w

    @property
    def h(self) -> float:
        return self._d.y

    @h.setter
    def h(self, new_h) -> None:
        self._d.y = new_h

    @property
    def wh(self) -> tuple[float]:
        return self._d.xy

    @wh.setter
    def wh(self, new_wh: Any) -> None:
        self._d.xy = new_wh
