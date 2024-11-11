import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minCost(*test_input)

    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]
        m = len(cuts)
        dp = [[0] * m for _ in range(m)]
        for i in range(m - 2, -1, -1):
            for j in range(i + 2, m):
                dp[i][j] = min(dp[i][k] + dp[k][j] for k in range(i + 1, j)) + cuts[j] - cuts[i]
        return dp[0][m - 1]

