import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.firstMissingPositive(test_input)

    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i, num in enumerate(nums):
            if num <= 0:
                nums[i] = n + 1
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])
        for i, num in enumerate(nums):
            if num > 0:
                return i + 1
        return n + 1
