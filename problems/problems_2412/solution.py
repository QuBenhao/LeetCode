import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumMoney(test_input)

    def minimumMoney(self, transactions: List[List[int]]) -> int:
        # Worst-case transaction order
        total_lose = 0
        mx = 0
        for cost, cashback in transactions:
            total_lose += max(cost - cashback, 0)
            # For a losing transaction, enough money must remain after all losses: init >= total_lose + cost - (cost - cashback) = total_lose + cashback
            # For a profitable transaction, enough money must remain after all losses: init >= total_lose + cost
            mx = max(mx, min(cost, cashback))
        return total_lose + mx
