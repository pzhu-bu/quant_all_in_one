from __future__ import annotations

import pandas as pd


def linear_transaction_cost(turnover: pd.Series, cost_bps: float) -> pd.Series:
    return turnover.abs() * cost_bps / 10_000.0
