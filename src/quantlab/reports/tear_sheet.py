from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ReportArtifact:
    title: str
    path: str
    artifact_type: str
