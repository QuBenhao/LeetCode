import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumMoney(test_input)

    def minimumMoney(self, transactions: List[List[int]]) -> int:
        # 最坏交易顺序
        total_lose = 0
        mx = 0
        for cost, cashback in transactions:
            total_lose += max(cost - cashback, 0)
            # 如果是亏钱的，那么至少需要在所有亏钱后依然足够，即 init >= total_lose + cost - (cost - cashback) = total_lose + cashback
            # 如果是赚钱的，那么至少需要在所有亏钱后依然足够，即 init >= total_lose + cost
            mx = max(mx, min(cost, cashback))
        return total_lose + mx
