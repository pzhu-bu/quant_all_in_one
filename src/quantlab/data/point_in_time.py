from __future__ import annotations

import pandas as pd

REQUIRED_POINT_IN_TIME_COLUMNS = frozenset({"symbol", "timestamp", "asof_timestamp"})


def assert_point_in_time_frame(frame: pd.DataFrame) -> None:
    missing = REQUIRED_POINT_IN_TIME_COLUMNS.difference(frame.columns)
    if missing:
        joined = ", ".join(sorted(missing))
        raise ValueError(f"missing point-in-time columns: {joined}")

    if (frame["asof_timestamp"] < frame["timestamp"]).any():
        raise ValueError("asof_timestamp must be greater than or equal to timestamp")
