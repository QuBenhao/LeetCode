import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countStableSubsequences(test_input)

    def countStableSubsequences(self, nums: List[int]) -> int:
        dp0 = dp1 = dp00 = dp01 = dp10 = dp11 = 0
        for num in nums:
            if num & 1:
                dp1, dp01, dp11 = (dp1 + 1) % MOD, (dp01 + dp0 + dp00 + dp10) % MOD, (dp11 + dp1 + dp01) % MOD
            else:
                dp0, dp00, dp10 = (dp0 + 1) % MOD, (dp00 + dp0 + dp10) % MOD, (dp10 + dp1 + dp01 + dp11) % MOD
        return (dp0 + dp1 + dp00 + dp01 + dp10 + dp11) % MOD

MOD = 10**9 + 7
