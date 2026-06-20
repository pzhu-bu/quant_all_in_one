from __future__ import annotations

import pandas as pd


def equity_curve(returns: pd.Series, initial_cash: float = 1.0) -> pd.Series:
    if initial_cash <= 0:
        raise ValueError("initial_cash must be positive")
    return initial_cash * (1.0 + returns.fillna(0.0)).cumprod()
