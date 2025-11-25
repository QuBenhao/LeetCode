import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfPaths(*test_input)

    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                for d in range(k):
                    v = (d + grid[i][j]) % k
                    if i > 0:
                        dp[i][j][v] = (dp[i][j][v] + dp[i-1][j][d]) % MOD
                    if j > 0:
                        dp[i][j][v] = (dp[i][j][v] + dp[i][j-1][d]) % MOD
        return dp[m-1][n-1][0]

MOD = 10 ** 9 + 7
