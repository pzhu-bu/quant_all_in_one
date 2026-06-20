from __future__ import annotations

import numpy as np
import pandas as pd


def annualized_sharpe(returns: pd.Series, periods_per_year: int = 252) -> float:
    clean = returns.dropna()
    if clean.empty or clean.std(ddof=1) == 0:
        return float("nan")
    return float(np.sqrt(periods_per_year) * clean.mean() / clean.std(ddof=1))
