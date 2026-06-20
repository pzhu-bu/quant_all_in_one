from __future__ import annotations

import pandas as pd


def forward_return(close: pd.Series, horizon: int) -> pd.Series:
    if horizon <= 0:
        raise ValueError("horizon must be positive")
    return close.shift(-horizon) / close - 1.0
