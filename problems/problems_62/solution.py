import solution
from typing import *
import math


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.uniquePaths(*test_input)

    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [1] * n
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[j] += dp[j-1]
        # return dp[n - 1]

        return math.comb(m + n - 2, n - 1)
