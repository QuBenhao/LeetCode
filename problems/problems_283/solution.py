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
        n = len(nums)
        left = 0
        while left < n and nums[left] != 0:
            left += 1
        right = left + 1
        while right < n:
            while right < n and nums[right] == 0:
                right += 1
            if right == n:
                break
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right += 1
