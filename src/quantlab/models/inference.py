from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

import pandas as pd


class Predictor(Protocol):
    def predict(self, features: pd.DataFrame) -> pd.Series: ...


@dataclass(frozen=True)
class InferenceRequest:
    feature_set: str
    asof_timestamp: str
