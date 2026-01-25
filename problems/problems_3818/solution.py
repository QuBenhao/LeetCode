import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumPrefixLength(test_input)

    def minimumPrefixLength(self, nums: List[int]) -> int:
        for i in range(len(nums) - 2, -1, -1):
            if nums[i + 1] <= nums[i]:
                return i + 1
        return 0
