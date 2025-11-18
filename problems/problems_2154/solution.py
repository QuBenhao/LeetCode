import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findFinalValue(*test_input)

    def findFinalValue(self, nums: List[int], original: int) -> int:
        s = set(nums)
        while original in s:
            original *= 2
        return original
