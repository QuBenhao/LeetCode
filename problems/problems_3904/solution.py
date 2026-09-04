from itertools import pairwise

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.firstStableIndex(*test_input)

    def firstStableIndex(self, nums: list[int], k: int) -> int:
        right_min = list(nums)
        n = len(nums)
        for i in range(n - 2, -1, -1):
            if right_min[i + 1] < right_min[i]:
                right_min[i] = right_min[i + 1]
        l = nums[0]
        for i in range(n):
            if nums[i] > l:
                l = nums[i]
            if l - right_min[i] <= k:
                return i
        return -1
