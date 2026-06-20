from __future__ import annotations


def annualize_funding_rate(periodic_rate: float, periods_per_year: int = 3 * 365) -> float:
    return (1.0 + periodic_rate) ** periods_per_year - 1.0
