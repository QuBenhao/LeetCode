import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canPartition(test_input)

    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        s //= 2
        dp = [False] * (s + 1)
        dp[0] = True
        for num in nums:
            for i in range(s, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[s]
