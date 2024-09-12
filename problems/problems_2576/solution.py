import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxNumOfMarkedIndices(test_input)

    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        for num in nums[(len(nums) + 1) // 2:]:
            if num >= 2 * nums[left]:
                left += 1
        return left * 2
