import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.new21Game(*test_input)

    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0.0] * (n + 1)
        s = 0.0
        for i in range(n, -1, -1):
            dp[i] = 1.0 if i >= k else s / maxPts
            s += dp[i]
            if i + maxPts <= n:
                s -= dp[i + maxPts]
        return dp[0]
