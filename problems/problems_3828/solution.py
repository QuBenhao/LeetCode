import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.finalElement(test_input)

    def finalElement(self, nums: List[int]) -> int:
        return max(nums[0], nums[-1])
