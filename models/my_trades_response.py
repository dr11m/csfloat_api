from typing import List, Optional
from pydantic import BaseModel

class Sticker(BaseModel):
    name: str
    price: Optional[float]  # Цена в `reference.price`
    wear: float = 0.0       # По умолчанию 0, если не указано

    @classmethod
    def from_raw(cls, raw: dict):
        return cls(
            name=raw.get("name"),
            price=raw.get("reference", {}).get("price"),
            wear=raw.get("wear", 0.0)
        )
    
    @property
    def normal_price(self) -> float:
        # Если цена существует, нормализуем её; если нет, возвращаем 0.0
        return round(self.price / 100, 2) if self.price is not None else 0.0
    

    def dict(self, *args, **kwargs):
        data = super().dict(*args, **kwargs)
        # Заменяем 'price' на 'normal_price' в итоговом словаре
        data['normal_price'] = self.normal_price
        # Убираем поле 'price', если оно не требуется
        del data['price']
        return data

class Item(BaseModel):
    float_value: Optional[float]
    market_hash_name: str
    stickers: Optional[List[Sticker]]

    @classmethod
    def from_raw(cls, raw: dict):
        stickers = raw.get("stickers")
        return cls(
            float_value=raw.get("float_value"),
            market_hash_name=raw.get("market_hash_name"),
            stickers=[Sticker.from_raw(sticker) for sticker in stickers] if stickers else None
        )
    
    @property
    def total_sticker_price(self) -> float:
        # Возвращаем сумму всех нормализованных цен наклеек или 0, если их нет
        if self.stickers:
            return sum(sticker.normal_price for sticker in self.stickers)
        return 0.0

class Contract(BaseModel):
    id: str
    price: int
    state: str
    item: Item

    @classmethod
    def from_raw(cls, raw: dict):
        return cls(
            id=raw["id"],
            price=raw["price"],
            state=raw["state"],
            item=Item.from_raw(raw["item"])
        )
    
    @property
    def normal_price(self) -> float:
        return round(self.price / 100, 2)

class Trade(BaseModel):
    id: str
    contract: Contract
    accepted_at: str  # 2024-12-06T23:35:14.672965Z
    state: str  # verified / failed / canceled

    @classmethod
    def from_raw(cls, raw: dict):
        return cls(
            id=raw["id"],
            contract=Contract.from_raw(raw["contract"]),
            accepted_at=raw["accepted_at"],
            state=raw["state"]
        )

class TradesResponse(BaseModel):
    trades: List[Trade]
    count: int

    @classmethod
    def from_raw(cls, raw: dict):
        return cls(
            trades=[Trade.from_raw(trade) for trade in raw.get("trades", [])],
            count=raw["count"]
        )


if __name__ == "__main__":
    import json

    # Пример ответа API (JSON из запроса)
    response_json = """{
    "trades": [
        {
        "id": "781627664392913197",
        "contract": {
            "id": "781546687553470972",
            "price": 1334,
            "state": "sold",
            "item": {
            "float_value": 0.0567,
            "market_hash_name": "AK-47 | Redline",
            "stickers": [
                {
                "name": "Crown (Foil)",
                "reference": {"price": 1250},
                "wear": 0.01
                },
                {
                "name": "Katowice 2014",
                "reference": {"price": 5000}
                }
            ]
            }
        }
        }
    ],
    "count": 1
    }"""

    # Десериализация
    data = json.loads(response_json)
    parsed = TradesResponse.from_raw(data)

    # Вывод результата
    print(parsed.model_dump_json(indent=4))
