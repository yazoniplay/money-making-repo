"""
Core market analyzer and opportunity scoring module integrating money_maker logic.
"""

import json
from src.money_maker import FinancialRecord, calculate_profit

class OpportunityAnalyzer:
    def __init__(self):
        self.records = [
            FinancialRecord(revenue=1000, cost=200),  # API Data Pipeline (Profit: 800)
            FinancialRecord(revenue=900, cost=0),     # Automated Newsletter (Profit: 900)
            FinancialRecord(revenue=500, cost=25)     # Micro-SaaS Plugin (Profit: 475)
        ]

    def evaluate(self):
        print("Evaluating opportunities via FinancialRecord profit metrics...")
        best = max(self.records, key=lambda x: x.profit())
        total = calculate_profit(self.records)
        return {"best_opportunity_profit": best.profit(), "total_projected_profit": total}

if __name__ == "__main__":
    analyzer = OpportunityAnalyzer()
    result = analyzer.evaluate()
    print(f"Evaluation result: {json.dumps(result, indent=2)}")
