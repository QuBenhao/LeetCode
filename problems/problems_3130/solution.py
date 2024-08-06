import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfStableArrays(*test_input)

    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[[0] * 2 for _ in range(one + 1)] for _ in range(zero + 1)]
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1] - (dp[i - limit - 1][j][1] if i > limit else 0)) % mod
                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1] - (dp[i][j - limit - 1][0] if j > limit else 0)) % mod
        return (dp[zero][one][0] + dp[zero][one][1]) % mod
