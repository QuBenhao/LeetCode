import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countPartitions(test_input)

    def countPartitions(self, nums: List[int]) -> int:
        s = sum(nums)
        return len(nums) - 1 if s % 2 == 0 else 0
