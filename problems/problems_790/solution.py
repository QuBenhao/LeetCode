import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numTilings(test_input)

    def numTilings(self, n: int) -> int:
        mod = 10**9 + 7
        # dp[i][j], i代表第i列, j代表第i列的状态 0: 空 1: 上面填了 2: 下面填了 3: 上下都填了
        dp = [[0] * 4 for _ in range(2)]
        dp[1][0] = dp[1][3] = 1
        for i in range(2, n + 1):
            prev, cur = (i - 1) % 2, i % 2
            dp[cur][0] = dp[prev][3] % mod
            dp[cur][1] = (dp[prev][0] + dp[prev][2]) % mod
            dp[cur][2] = (dp[prev][0] + dp[prev][1]) % mod
            dp[cur][3] = sum(v for v in dp[prev]) % mod
        return dp[n % 2][3] % mod
