from itertools import pairwise

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isTrionic(test_input)

    def isTrionic(self, nums: List[int]) -> bool:
        # The first segment must be increasing
        if nums[0] >= nums[1]:
            return False
        cur = 1
        t = 0
        for a, b in pairwise(nums):
            if a == b:
                return False
            # Not a turning point
            if (a < b) == (cur == 1):
                continue
            # Turning point
            cur ^= 1
            t += 1
            # Optimize with an early return
            if t > 2:
                return False
        return t == 2
