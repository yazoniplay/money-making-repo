"""Core money calculation utilities.

This module provides a very small but extensible framework for
calculating profit. It supports FinancialRecord dataclasses and
clean single-iterable profit summation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

@dataclass
class FinancialRecord:
    """Simple data holder for revenue and cost."""
    revenue: float
    cost: float

    def profit(self) -> float:
        """Return the profit for this record."""
        return self.revenue - self.cost

def calculate_profit(records: Iterable[FinancialRecord]) -> float:
    """Calculate total profit from an iterable of FinancialRecords.

    Parameters
    ----------
    records
        An iterable collection of :class:`FinancialRecord`.

    Returns
    -------
    float
        The summed profit across all provided records.
    """
    return sum(record.profit() for record in records)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python -m src.money_maker revenue cost", file=sys.stderr)
        sys.exit(1)
    rev, cost = float(sys.argv[1]), float(sys.argv[2])
    record = FinancialRecord(revenue=rev, cost=cost)
    print(f"Profit: {record.profit():.2f}")
