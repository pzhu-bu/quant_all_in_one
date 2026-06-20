from __future__ import annotations

import pandas as pd


def cross_sectional_rank(values: pd.Series) -> pd.Series:
    return values.rank(method="average", pct=True)
