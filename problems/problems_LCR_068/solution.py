import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.searchInsert(*test_input)

    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
