from __future__ import annotations


def require_quantlib() -> None:
    try:
        import QuantLib  # noqa: F401
    except ImportError as exc:
        raise RuntimeError("QuantLib-Python is required for this adapter") from exc
