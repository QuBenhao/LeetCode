import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.champagneTower(*test_input)

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [poured]
        for i in range(1, query_row + 1):
            next_dp = [0.0] * (i + 1)
            for j in range(i):
                if dp[j] > 1:
                    excess = (dp[j] - 1) / 2
                    next_dp[j] += excess
                    next_dp[j + 1] += excess
            dp = next_dp
        return min(1.0, dp[query_glass])
