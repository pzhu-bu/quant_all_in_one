# C++ Core

The C++ layer is for stable, benchmarked kernels that need predictable latency or high throughput.

Initial modules:

- `factor_engine`: rank, winsorize, neutralize, Arrow-oriented factor transforms
- `optimizer`: long-only and constrained optimization kernels
- `event_engine`: event-driven backtesting and broker simulation primitives
- `risk_engine`: pre-trade and daily risk calculations
- `bsm`: small pricing models used for tests and parity checks

Keep Python parity tests when adding pybind11 bindings.
