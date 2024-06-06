import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        self.moveZeroes(test_input)
        return test_input

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for num in nums:
            if num != 0:
                nums[idx] = num
                idx += 1
        for i in range(idx, len(nums)):
            nums[i] = 0
