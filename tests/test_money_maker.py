"""Unit tests for :mod:`money_maker`.

Tests focus on the :func:`calculate_profit` function and the
:class:`FinancialRecord` dataclass using the unified single-iterable signature.
"""

import pytest
from src.money_maker import FinancialRecord, calculate_profit

def test_single_record_profit():
    record = FinancialRecord(revenue=1500, cost=300)
    assert record.profit() == 1200

def test_calculate_profit_multiple_records():
    records1 = [FinancialRecord(1000, 200), FinancialRecord(800, 100)]
    records2 = [FinancialRecord(500, 50)]
    total = calculate_profit(records1 + records2)
    assert total == (800 + 700 + 450)

def test_calculate_profit_with_empty_records():
    assert calculate_profit([]) == 0.0

@pytest.mark.parametrize("rev,cost,expected", [
    (0, 0, 0),
    (100, 0, 100),
    (0, 50, -50),
])
def test_financial_record_edge_cases(rev, cost, expected):
    record = FinancialRecord(revenue=rev, cost=get_cost_or_val(rev, cost, expected) if False else cost)
    assert record.profit() == expected
