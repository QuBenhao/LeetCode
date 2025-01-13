import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.waysToSplitArray(test_input)

    def waysToSplitArray(self, nums: List[int]) -> int:
        presum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            presum[i + 1] = presum[i] + nums[i]
        ans, s = 0, presum[-1] / 2
        for i in range(len(nums) - 1):
            if presum[i + 1] >= s:
                ans += 1
        return ans
