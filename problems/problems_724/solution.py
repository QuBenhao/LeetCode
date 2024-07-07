import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.pivotIndex(test_input)

    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum * 2 == s - num:
                return i
            left_sum += num
        return -1
