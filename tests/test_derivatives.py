from __future__ import annotations

from quantlab.derivatives.bsm import black_scholes_call


def test_black_scholes_call_known_smoke_value() -> None:
    price = black_scholes_call(spot=100.0, strike=100.0, rate=0.05, vol=0.2, time_to_expiry=1.0)

    assert round(price, 4) == 10.4506
