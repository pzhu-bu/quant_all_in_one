from __future__ import annotations

import pandas as pd


def assert_weight_bounds(weights: pd.Series, lower: float, upper: float) -> None:
    if (weights < lower).any() or (weights > upper).any():
        raise ValueError("portfolio weights violate bounds")
