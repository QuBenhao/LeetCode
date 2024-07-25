import solution
from typing import *
from itertools import pairwise


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findValueOfPartition(test_input)

    def findValueOfPartition(self, nums: List[int]) -> int:
        return min(b - a for a, b in pairwise(sorted(nums)))
