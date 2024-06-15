import solution
from typing import *
from math import inf


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxScore(*test_input)

    def maxScore(self, nums: List[int], x: int) -> int:
        ans = nums[0]
        dp = [-inf, -inf]
        dp[nums[0] % 2] = nums[0]
        for num in nums[1:]:
            idx = num % 2
            cur = max(dp[idx] + num, dp[idx ^ 1] + num - x)
            ans = max(ans, cur)
            dp[idx] = max(dp[idx], cur)
        return ans
