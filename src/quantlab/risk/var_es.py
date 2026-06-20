from __future__ import annotations

import pandas as pd


def historical_var(returns: pd.Series, confidence: float = 0.95) -> float:
    if not 0 < confidence < 1:
        raise ValueError("confidence must be between 0 and 1")
    return float(-returns.dropna().quantile(1.0 - confidence))
