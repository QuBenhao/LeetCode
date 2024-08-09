import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canJump(test_input)

    def canJump(self, nums: List[int]) -> bool:
        max_idx = 0
        for i, dis in enumerate(nums):
            max_idx = max(max_idx, i + dis)
            if max_idx >= len(nums) - 1:
                return True
            if i >= max_idx:
                return False
        return max_idx >= len(nums) - 1
