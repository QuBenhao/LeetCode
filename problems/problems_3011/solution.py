import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canSortArray(test_input)

    def canSortArray(self, nums: List[int]) -> bool:
        n, idx, pre_max = len(nums), 0, 0
        while idx < n:
            ones, cur_max = nums[idx].bit_count(), nums[idx]
            while idx < n and nums[idx].bit_count() == ones:
                if nums[idx] < pre_max:
                    return False
                cur_max = max(cur_max, nums[idx])
                idx += 1
            pre_max = cur_max
        return True
