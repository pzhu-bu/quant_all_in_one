from __future__ import annotations

import numpy as np
import pandas as pd


def winsorize(values: pd.Series, lower: float = 0.01, upper: float = 0.99) -> pd.Series:
    if not 0 <= lower < upper <= 1:
        raise ValueError("expected 0 <= lower < upper <= 1")
    return values.clip(lower=values.quantile(lower), upper=values.quantile(upper))


def neutralize(values: pd.Series, exposures: pd.DataFrame) -> pd.Series:
    aligned = pd.concat([values.rename("_target"), exposures], axis=1).dropna()
    if aligned.empty:
        return pd.Series(index=values.index, dtype=float)

    y = aligned["_target"].to_numpy(dtype=float)
    X = aligned.drop(columns="_target").to_numpy(dtype=float)
    X = np.column_stack([np.ones(len(X)), X])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    residuals = y - X @ beta

    result = pd.Series(index=values.index, dtype=float)
    result.loc[aligned.index] = residuals
    return result
