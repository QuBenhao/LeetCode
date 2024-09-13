import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.singleNonDuplicate(test_input)

    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == nums[mid ^ 1]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
