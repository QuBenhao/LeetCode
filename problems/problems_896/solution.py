import solution
from typing import *
from itertools import pairwise


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isMonotonic(test_input)

    def isMonotonic(self, nums: List[int]) -> bool:
        inc, dec = False, False
        for a, b in pairwise(nums):
            if a > b:
                if dec:
                    return False
                inc = True
            elif a < b:
                if inc:
                    return False
                dec = True
        return True

