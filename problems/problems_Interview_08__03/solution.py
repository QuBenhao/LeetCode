import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findMagicIndex(test_input)

    def findMagicIndex(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                return i
            i = max(nums[i], i + 1)
        return -1
