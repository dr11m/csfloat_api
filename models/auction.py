from typing import Dict, Any, Optional


class TopBid:
    __slots__ = (
        "_id",
        "_created_at",
        "_price",
        "_contract_id",
        "_state",
        "_active",
        "_obfuscated_buyer_id"
    )

    def __init__(self, *, data: Dict[str, Any]):
        self._id = data.get("id")
        self._created_at = data.get("created_at")
        self._price = data.get("price")
        self._contract_id = data.get("contract_id")
        self._state = data.get("state")
        self._active = data.get("active")
        self._obfuscated_buyer_id = data.get("obfuscated_buyer_id")

    @property
    def id(self) -> Optional[int]:
        return self._id

    @property
    def created_at(self) -> Optional[str]:
        return self._created_at

    @property
    def price(self) -> Optional[int]:
        return self._price

    @property
    def contract_id(self) -> Optional[str]:
        return self._contract_id

    @property
    def state(self) -> Optional[str]:
        return self._state

    @property
    def obfuscated_buyer_id(self) -> Optional[str]:
        return self._obfuscated_buyer_id


class AuctionDetails:
    __slots__ = (
        "_reserve_price",
        "_top_bid",
        "_expires_at",
        "_min_next_bid",
    )

    def __init__(self, *, data: Dict[str, Any]):
        self._reserve_price = data.get("reserve_price")
        self._top_bid = data.get("top_bid")
        self._expires_at = data.get("expires_at")
        self._min_next_bid = data.get("min_next_bid")

    @property
    def reserve_price(self) -> Optional[float]:
        return self._reserve_price

    @property
    def top_bid(self) -> Optional[TopBid]:
        return TopBid(data=self._top_bid)

    @property
    def expires_at(self) -> Optional[str]:
        return self._expires_at

    @property
    def min_next_bid(self) -> Optional[float]:
        return self._min_next_bid
