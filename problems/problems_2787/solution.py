import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfWays(*test_input)

    def numberOfWays(self, n: int, x: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            v = i ** x
            if v > n:
                break
            for j in range(n, v - 1, -1):
                dp[j] = (dp[j] + dp[j - v]) % MOD
        return dp[n]

MOD = 10**9 + 7
