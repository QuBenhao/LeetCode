from itertools import pairwise

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.firstStableIndex(*test_input)

    def firstStableIndex(self, nums: list[int], k: int) -> int:
        left_max, right_min = list(nums), list(nums)
        n = len(nums)
        for i in range(n - 1):
            if left_max[i] > left_max[i + 1]:
                left_max[i + 1] = left_max[i]
        for i in range(n - 2, -1, -1):
            if right_min[i + 1] < right_min[i]:
                right_min[i] = right_min[i + 1]
        for i in range(n):
            if left_max[i] - right_min[i] <= k:
                return i
        return -1
