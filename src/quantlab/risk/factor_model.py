from __future__ import annotations

import pandas as pd


def factor_portfolio_exposure(weights: pd.Series, exposures: pd.DataFrame) -> pd.Series:
    aligned = exposures.reindex(weights.index).fillna(0.0)
    return aligned.mul(weights, axis=0).sum(axis=0)
