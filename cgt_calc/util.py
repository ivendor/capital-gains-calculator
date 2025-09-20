"""Utility functions."""

import decimal
from decimal import Decimal


def round_decimal(value: Decimal, digits: int = 0) -> Decimal:
    """Round decimal to given precision."""
    with decimal.localcontext() as ctx:
        ctx.rounding = decimal.ROUND_HALF_UP
        return Decimal(round(value, digits))


def strip_zeros(value: Decimal) -> str:
    """Strip trailing zeros from Decimal."""
    return f"{value:.10f}".rstrip("0").rstrip(".")


def approx_equal(val_a: Decimal, val_b: Decimal) -> bool:
    """Calculate if two decimal are the same within 0.01.

    It is not clear how Schwab or other brokers round the dollar value,
    so assume the values are equal if they are within 0.01.
    """
    return abs(val_a - val_b) < Decimal("0.01")
