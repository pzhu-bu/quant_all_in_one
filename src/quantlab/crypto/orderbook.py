from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Level:
    price: float
    size: float
