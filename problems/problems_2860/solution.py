from itertools import pairwise

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countWays(test_input)

    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        # i people are selected: everyone at or below x is selected, and everyone at or above y is not
        return int(nums[0] > 0) + sum(x < i < y for i, (x, y) in enumerate(pairwise(nums), 1)) + 1
