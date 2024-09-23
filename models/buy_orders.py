from typing import Optional, Dict, Any

class BuyOrders:
    __slots__ = (
        "_id",
        "_created_at",
        "_expression",
        "_qty",
        "_price"
    )

    def __init__(self, *, data: Dict[str, Any]):
        self._id = data.get("id")
        self._created_at = data.get("created_at")
        self._expression = data.get("expression")
        self._qty = data.get("qty")
        self._price = data.get("price")

    @property
    def id(self) -> Optional[str]:
        return self._id

    @property
    def created_at(self) -> Optional[str]:
        return self._created_at

    @property
    def expression(self) -> Optional[str]:
        return self._expression

    @property
    def qty(self) -> Optional[int]:
        return self._qty

    @property
    def price(self) -> Optional[int]:
        return self._price