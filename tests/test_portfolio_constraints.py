from __future__ import annotations

import pandas as pd
import pytest

from quantlab.portfolio.constraints import assert_weight_bounds


def test_weight_bounds_rejects_oversized_position() -> None:
    weights = pd.Series({"A": 0.03, "B": 0.07})

    with pytest.raises(ValueError, match="bounds"):
        assert_weight_bounds(weights, lower=0.0, upper=0.05)
