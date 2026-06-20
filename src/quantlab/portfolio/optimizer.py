from __future__ import annotations

import pandas as pd


def normalize_long_only_weights(scores: pd.Series) -> pd.Series:
    positive = scores.clip(lower=0.0)
    total = positive.sum()
    if total <= 0:
        return pd.Series(0.0, index=scores.index)
    return positive / total
