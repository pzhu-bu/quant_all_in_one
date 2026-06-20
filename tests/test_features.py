from __future__ import annotations

import pandas as pd

from quantlab.features.factors import cross_sectional_rank
from quantlab.features.neutralize import neutralize, winsorize


def test_cross_sectional_rank_returns_percentiles() -> None:
    values = pd.Series({"A": 3.0, "B": 1.0, "C": 2.0})

    ranked = cross_sectional_rank(values)

    assert ranked.to_dict() == {"A": 1.0, "B": 1 / 3, "C": 2 / 3}


def test_winsorize_clips_tails() -> None:
    values = pd.Series([0.0, 1.0, 100.0])

    clipped = winsorize(values, lower=0.0, upper=0.5)

    assert clipped.iloc[-1] == 1.0


def test_neutralize_returns_residuals_with_original_index() -> None:
    values = pd.Series({"A": 1.0, "B": 2.0, "C": 3.0})
    exposures = pd.DataFrame({"size": [1.0, 2.0, 3.0]}, index=values.index)

    residuals = neutralize(values, exposures)

    assert list(residuals.index) == ["A", "B", "C"]
    assert residuals.abs().max() < 1e-12
