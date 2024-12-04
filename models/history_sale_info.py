from pydantic import BaseModel
from typing import Optional, List, Union
from datetime import datetime


class Reference(BaseModel):
    base_price: int
    float_factor: float
    predicted_price: int
    quantity: int
    last_updated: datetime

class Sticker(BaseModel):
    stickerId: int
    slot: int
    icon_url: str
    name: str
    reference: Optional[dict] = None

class Item(BaseModel):
    asset_id: str
    def_index: int
    paint_index: Optional[int] = None
    paint_seed: Optional[int] = None
    float_value: Optional[float] = None
    icon_url: str
    d_param: Optional[str] = None
    is_stattrak: Optional[bool] = None
    is_souvenir: Optional[bool] = None
    rarity: int
    quality: Optional[int] = None
    market_hash_name: str
    stickers: Optional[List[Sticker]] = None
    tradable: int
    inspect_link: Optional[str] = None
    has_screenshot: bool
    cs2_screenshot_id: Optional[str] = None
    cs2_screenshot_at: Optional[datetime] = None
    is_commodity: bool
    type: str
    rarity_name: str
    type_name: str
    item_name: str
    wear_name: Optional[str] = None
    description: Optional[str] = None
    collection: Optional[str] = None 
    serialized_inspect: Optional[str] = None
    gs_sig: Optional[str] = None

class ItemSale(BaseModel):
    id: str
    created_at: datetime
    type: str
    price: int
    state: str
    reference: Union[Reference, dict]
    item: Item
    is_seller: bool
    is_watchlisted: bool
    watchers: int
    sold_at: datetime

    @property
    def sold_at_ts(self) -> int:
        return int(self.sold_at.timestamp())
    
    @property
    def price_normal(self) -> float:
        return round(self.price / 100, 2)



    