from __future__ import annotations

import pandas as pd
import pytest

from quantlab.data.point_in_time import assert_point_in_time_frame


def test_point_in_time_frame_rejects_future_visibility() -> None:
    frame = pd.DataFrame(
        {
            "symbol": ["AAPL"],
            "timestamp": [pd.Timestamp("2024-01-02T16:00:00Z")],
            "asof_timestamp": [pd.Timestamp("2024-01-02T15:59:00Z")],
        }
    )

    with pytest.raises(ValueError, match="asof_timestamp"):
        assert_point_in_time_frame(frame)
