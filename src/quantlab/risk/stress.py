from __future__ import annotations

import pandas as pd


def apply_return_shock(prices: pd.Series, shock: float) -> pd.Series:
    return prices * (1.0 + shock)
