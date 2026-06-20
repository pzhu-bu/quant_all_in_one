from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RiskLimit:
    name: str
    threshold: float

    def check(self, value: float) -> bool:
        return value <= self.threshold
