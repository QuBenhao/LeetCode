import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.change(*test_input)

    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i - c]
        return dp[-1]
