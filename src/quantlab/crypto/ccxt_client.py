from __future__ import annotations


def require_ccxt() -> None:
    try:
        import ccxt  # noqa: F401
    except ImportError as exc:
        raise RuntimeError("ccxt is required for crypto connectivity") from exc
