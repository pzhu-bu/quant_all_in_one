from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TrainingRun:
    name: str
    dataset_version: str
    feature_set: str
    model_family: str
