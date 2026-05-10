import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumJumps(*test_input)

    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0
        for j in range(1, n):
            for i in range(j):
                if dp[i] != -1 and abs(nums[j] - nums[i]) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)
        return dp[-1]
