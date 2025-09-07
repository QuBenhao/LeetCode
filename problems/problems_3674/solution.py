import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minOperations(test_input)

    def minOperations(self, nums: List[int]) -> int:
        return int(not all(x == nums[0] for x in nums))
