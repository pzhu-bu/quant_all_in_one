from __future__ import annotations

import pandas as pd


def assert_feature_parity(training_columns: list[str], inference_frame: pd.DataFrame) -> None:
    missing = set(training_columns).difference(inference_frame.columns)
    extra = set(inference_frame.columns).difference(training_columns)
    if missing or extra:
        raise ValueError(f"feature mismatch: missing={sorted(missing)}, extra={sorted(extra)}")
