import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxOperations(test_input)

    def maxOperations(self, nums: List[int]) -> int:
        s = nums[0] + nums[1]
        for idx in range(0, len(nums) - 1, 2):
            if nums[idx] + nums[idx + 1] != s:
                return idx // 2
        return len(nums) // 2
