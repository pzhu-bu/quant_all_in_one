from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class TradingCalendar:
    name: str
    sessions: frozenset[date]

    @classmethod
    def from_sessions(cls, name: str, sessions: Iterable[date]) -> TradingCalendar:
        return cls(name=name, sessions=frozenset(sessions))

    def is_session(self, value: date) -> bool:
        return value in self.sessions
