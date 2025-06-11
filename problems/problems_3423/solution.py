import solution
from typing import *
from itertools import pairwise


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxAdjacentDistance(test_input)

    def maxAdjacentDistance(self, nums: List[int]) -> int:
        ans = abs(nums[0] - nums[-1])
        for a, b in pairwise(nums):
            ans = max(ans, abs(a - b))
        return ans
