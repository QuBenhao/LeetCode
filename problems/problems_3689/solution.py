import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxTotalValue(*test_input)

    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return k * (max(nums) - min(nums))

