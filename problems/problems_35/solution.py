import solution
from typing import *
import bisect


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.searchInsert(*test_input)

    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)
