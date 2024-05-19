import solution
from typing import *
import bisect


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumCount(test_input)

    def maximumCount(self, nums: List[int]) -> int:
        left, right = bisect.bisect_left(nums, 0), bisect.bisect_right(nums, 0)
        return max(0, left, len(nums) - right)
