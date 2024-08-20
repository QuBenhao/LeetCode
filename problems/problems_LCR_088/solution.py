import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minCostClimbingStairs(test_input)

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[-1]
