import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.missingNumber(test_input)

    def missingNumber(self, nums: List[int]) -> int:
        return (n := len(nums)) * (n + 1) // 2 - sum(nums)

