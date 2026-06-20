from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class MarketEvent:
    timestamp: datetime
    symbol: str
    price: float
    volume: float
