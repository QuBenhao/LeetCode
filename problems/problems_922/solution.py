import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sortArrayByParityII(test_input)

    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j = 0, 1
        while i < n and j < n:
            while i < n and nums[i] % 2 == 0:
                i += 2
            while j < n and nums[j] % 2:
                j += 2
            if i < n and j < n:
                nums[i], nums[j] = nums[j], nums[i]
        return nums
