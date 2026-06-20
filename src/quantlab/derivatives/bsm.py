from __future__ import annotations

from math import erf, exp, log, sqrt


def _norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + erf(x / sqrt(2.0)))


def black_scholes_call(
    spot: float,
    strike: float,
    rate: float,
    vol: float,
    time_to_expiry: float,
) -> float:
    if min(spot, strike, vol, time_to_expiry) <= 0:
        raise ValueError("spot, strike, vol, and time_to_expiry must be positive")

    d1 = (log(spot / strike) + (rate + 0.5 * vol * vol) * time_to_expiry) / (
        vol * sqrt(time_to_expiry)
    )
    d2 = d1 - vol * sqrt(time_to_expiry)
    return spot * _norm_cdf(d1) - strike * exp(-rate * time_to_expiry) * _norm_cdf(d2)
