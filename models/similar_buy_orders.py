from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class SimilarBuyOrder(BaseModel):
    market_hash_name: str
    qty: int
    price: int

    @property
    def human_price(self) -> float:
        return float(self.price / 100)

class SimilarBuyOrders(BaseModel):
    data: List[SimilarBuyOrder]