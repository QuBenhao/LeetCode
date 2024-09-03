from itertools import pairwise

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countWays(test_input)

    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        # 当前选了i个人, x及以下的人都选了，y及以上的人都没选
        return int(nums[0] > 0) + sum(x < i < y for i, (x, y) in enumerate(pairwise(nums), 1)) + 1
