from __future__ import annotations

import pandas as pd
import pytest

from quantlab.backtest.vectorized import equity_curve


def test_equity_curve_compounds_returns() -> None:
    returns = pd.Series([0.10, -0.10])

    curve = equity_curve(returns, initial_cash=100.0)

    assert curve.iloc[-1] == pytest.approx(99.0)
