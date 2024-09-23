from typing import Dict, Any, Optional
from .seller import Seller
from .reference import Reference
from .item import Item
from .auction import AuctionDetails


class Listing:

    __slots__ = (
        "_id",
        "_created_at",
        "_type",
        "_price",
        "_description",
        "_state",
        "_seller",
        "_reference",
        "_item",
        "_is_seller",
        "_min_offer_price",
        "_max_offer_discount",
        "_is_watchlisted",
        "_watchers",
        "_auction_details",
        "_sold_at"
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._id = data.get("id", "")
        self._created_at = data.get("created_at")
        self._type = data.get("type", "")
        self._price = data.get("price")
        self._description = data.get("description")
        self._state = data.get("state", "")
        self._seller = data.get("seller")
        self._reference = data.get("reference")
        self._item = data.get("item")
        self._is_seller = data.get("is_seller", False)
        self._min_offer_price = data.get("min_offer_price")
        self._max_offer_discount = data.get("max_offer_discount")
        self._is_watchlisted = data.get("is_watchlisted", False)
        self._watchers = data.get("watchers", 0)
        self._auction_details = data.get("auction_details")
        self._sold_at = data.get("sold_at")

    @property
    def id(self) -> Optional[int]:
        return self._id

    @property
    def created_at(self) -> Optional[str]:
        return self._created_at

    @property
    def type(self) -> Optional[str]:
        return self._type

    @property
    def price(self) -> Optional[float]:
        return self._price

    @property
    def description(self) -> Optional[str]:
        return self._description

    @property
    def state(self) -> Optional[str]:
        return self._state

    @property
    def seller(self) -> Optional[Seller]:
        return Seller(data=self._seller)

    @property
    def reference(self) -> Optional[Reference]:
        return Reference(data=self._reference)

    @property
    def item(self) -> Optional[Item]:
        return Item(data=self._item)

    @property
    def is_seller(self) -> Optional[bool]:
        return self._is_seller

    @property
    def min_offer_price(self) -> Optional[float]:
        return self._min_offer_price

    @property
    def max_offer_discount(self) -> Optional[float]:
        return self._max_offer_discount

    @property
    def is_watchlisted(self) -> Optional[bool]:
        return self._is_watchlisted

    @property
    def watchers(self) -> Optional[int]:
        return self._watchers

    @property
    def auction_details(self) -> Optional[AuctionDetails]:
        return AuctionDetails(data=self._auction_details)

    @property
    def sold_at(self) -> Optional[str]:
        return self._sold_at
