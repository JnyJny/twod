"""w and h properties for CRect (deprecated along with CRect)"""

from typing import Any

from ..cpoint import CPoint as Point


class MixinDimension:
    _d: Point

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
    def wh(self) -> tuple[float, float]:
        return self._d.xy

    @wh.setter
    def wh(self, new_wh: Any) -> None:
        self._d.xy = new_wh
