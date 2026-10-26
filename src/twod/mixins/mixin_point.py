"""x and y properties for CRect (deprecated along with CRect)"""

from typing import Any

from ..cpoint import CPoint as Point


class MixinPoint:
    _p: Point

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
