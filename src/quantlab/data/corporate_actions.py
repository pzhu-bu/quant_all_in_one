from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class CorporateAction:
    symbol: str
    effective_date: date
    action_type: str
    adjustment_factor: float
