import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumTotal(test_input)

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [0] * n
        for i, nums in enumerate(triangle):
            if i > 0:
                dp[i] = dp[i - 1] + nums[i]
            for j in range(i-1, 0, -1):
                dp[j] = min(dp[j], dp[j - 1]) + nums[j]
            dp[0] += nums[0]
        return min(dp)
