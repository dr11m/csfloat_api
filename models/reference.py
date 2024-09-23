from typing import Dict, Any, Optional


class Reference:
    __slots__ = (
        "_base_price",
        "_float_factor",
        "_predicted_price",
        "_quantity",
        "_last_updated"
    )

    def __init__(self, *, data: Dict[str, Any]):
        self._base_price = data.get("base_price")
        self._float_factor = data.get("float_factor")
        self._predicted_price = data.get("predicted_price")
        self._quantity = data.get("quantity")
        self._last_updated = data.get("last_updated")

    @property
    def base_price(self) -> Optional[float]:
        return self._base_price

    @property
    def float_factor(self) -> Optional[float]:
        return self._float_factor

    @property
    def predicted_price(self) -> Optional[float]:
        return self._predicted_price

    @property
    def quantity(self) -> Optional[int]:
        return self._quantity

    @property
    def last_updated(self) -> Optional[str]:
        return self._last_updated
