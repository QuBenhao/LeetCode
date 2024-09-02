import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxStrength(test_input)

    def maxStrength(self, nums: List[int]) -> int:
        mx = mn = nums[0]
        for num in nums[1:]:
            mx, mn = max(mx, num, num * mx, num * mn), min(mn, num, num * mx, num * mn)
        return mx
