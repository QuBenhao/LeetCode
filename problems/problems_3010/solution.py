from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumCost(test_input)

    def minimumCost(self, nums: List[int]) -> int:
        min_v, second_min_v = inf, inf
        for i in range(1, len(nums)):
            if nums[i] < min_v:
                min_v, second_min_v = nums[i], min_v
            elif nums[i] < second_min_v:
                second_min_v = nums[i]
        return nums[0] + min_v + second_min_v
