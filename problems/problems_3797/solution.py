from math import isqrt

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfRoutes(*test_input)

    def numberOfRoutes(self, grid: List[str], d: int) -> int:
        n, m = len(grid), len(grid[0])
        D = isqrt(max(0, d * d - 1))

        dp = [1 if grid[n - 1][j] == "." else 0 for j in range(m)]
        for r in range(n - 1, -1, -1):
            f = [0] * (m + 1)
            for i in range(m):
                f[i + 1] = (f[i] + dp[i]) % MOD

            res = [0] * m
            for k in range(m):
                if grid[r][k] == ".":
                    res[k] = (f[min(m - 1, k + d) + 1] - f[max(0, k - d)]) % MOD

            g = [0] * (m + 1)
            for i in range(m):
                g[i + 1] = (g[i] + res[i]) % MOD

            ndp = [0] * m
            for t in range(m):
                if grid[r - 1][t] == ".":
                    ndp[t] = (g[min(m - 1, t + D) + 1] - g[max(0, t - D)]) % MOD

            dp = ndp
        return sum(res) % MOD

MOD = 10**9 + 7
