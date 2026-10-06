import solution
from typing import *
from math import inf


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxProduct(test_input)

    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        # dp[i][0] is the minimum product of a subarray ending at i
        # dp[i][1] is the maximum product of a subarray ending at i
        dp = [[inf, -inf] for _ in range(n)]
        dp[0] = [nums[0], nums[0]]
        ans = nums[0]
        for i in range(1, n):
            dp[i][0] = min(dp[i-1][0] * nums[i], dp[i-1][1] * nums[i], nums[i])
            dp[i][1] = max(dp[i-1][0] * nums[i], dp[i-1][1] * nums[i], nums[i])
            ans = max(ans, dp[i][1])
        return ans
