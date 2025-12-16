import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.waysToStep(test_input)

    def waysToStep(self, n: int) -> int:
        dp = [1, 2, 4, 0]
        for i in range(3, n):
            dp[i % 4] = ((dp[(i + 1) % 4] + dp[(i + 2) % 4]) % MOD + dp[(i + 3) % 4]) % MOD
        return dp[(n - 1) % 4]

MOD = 10 ** 9 + 7
