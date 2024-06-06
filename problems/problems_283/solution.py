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
        left = 0
        for idx, num in enumerate(nums):
            if num != 0:
                nums[left], nums[idx] = num, nums[left]
                left += 1
