import solution
from typing import *
import bisect


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.searchRange(*test_input)

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target)
        return [left, right - 1] if left < len(nums) and nums[left] == target else [-1, -1]
