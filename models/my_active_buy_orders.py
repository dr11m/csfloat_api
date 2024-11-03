from pydantic import BaseModel
from typing import List

class BuyOrder(BaseModel):
    id: str
    created_at: str  # можно использовать datetime, если требуется преобразование
    market_hash_name: str
    qty: int
    price: int

    @property
    def human_price(self) -> float:
        return float(self.price / 100)

class MyBuyOrdersResponse(BaseModel):
    orders: List[BuyOrder]
    count: int