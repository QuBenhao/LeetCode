import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countMaxOrSubsets(test_input)

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = mx = 0
        n = len(nums)
        mask = 1 << n
        dp = [0] * mask
        for i in range(1, mask):
            lowbit = i & -i
            prev, idx = i - lowbit, lowbit.bit_length() - 1
            dp[i] = dp[prev] | nums[idx]
            if dp[i] > mx:
                mx = dp[i]
                ans = 1
            elif dp[i] == mx:
                ans += 1
        return ans
