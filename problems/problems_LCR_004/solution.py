import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.singleNumber(test_input)

    def singleNumber(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2
