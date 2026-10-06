from functools import cache
from math import inf
import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumTotalCost(test_input)

    def maximumTotalCost(self, nums: List[int]) -> int:
        n = len(nums)
        # For subarrays longer than 2, the total cost is unchanged by splitting (the corresponding elements keep the same signs)
        f0, f1 = nums[0], nums[0] # f0 means the previous element was taken with a negative sign; f1 means it was taken with a positive sign
        for i in range(1, n):
            f0, f1 = f1 - nums[i], max(f0, f1) + nums[i]
        return max(f0, f1)
