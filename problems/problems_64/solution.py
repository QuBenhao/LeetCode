import solution
from typing import *
from itertools import accumulate


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minPathSum(test_input)

    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = list(accumulate(grid[0]))
        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[-1]
