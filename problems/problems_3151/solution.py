import solution
from typing import *
from itertools import pairwise


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isArraySpecial(test_input)

    def isArraySpecial(self, nums: List[int]) -> bool:
        return all(a & 1 != b & 1 for a, b in pairwise(nums))
