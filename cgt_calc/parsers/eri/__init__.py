"""Parse ERI input files."""

from __future__ import annotations

from typing import TYPE_CHECKING

from .raw import read_eri_raw

if TYPE_CHECKING:
    from .model import EriTransaction


def read_eri_transactions(
    eri_raw_file: str | None,
) -> list[EriTransaction]:
    """Read Excess Reported Income transactions for all funds."""
    transactions = []

    if eri_raw_file is not None:
        transactions += read_eri_raw(eri_raw_file)
    else:
        print("INFO: No ERI raw file provided")

    return transactions
