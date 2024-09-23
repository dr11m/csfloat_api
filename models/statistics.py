from typing import Dict, Any, Optional


class Statistics:
    __slots__ = (
        "_median_trade_time",
        "_total_avoided_trades",
        "_total_failed_trades",
        "_total_trades",
        "_total_verified_trades"
    )

    def __init__(self, *, data: Dict[str, Any]):
        self._median_trade_time = data.get("median_trade_time")
        self._total_avoided_trades = data.get("total_avoided_trades")
        self._total_failed_trades = data.get("total_failed_trades")
        self._total_trades = data.get("total_trades")
        self._total_verified_trades = data.get("total_verified_trades")

    @property
    def median_trade_time(self) -> Optional[float]:
        return self._median_trade_time

    @property
    def total_avoided_trades(self) -> Optional[int]:
        return self._total_avoided_trades

    @property
    def total_failed_trades(self) -> Optional[int]:
        return self._total_failed_trades

    @property
    def total_trades(self) -> Optional[int]:
        return self._total_trades

    @property
    def total_verified_trades(self) -> Optional[int]:
        return self._total_verified_trades
