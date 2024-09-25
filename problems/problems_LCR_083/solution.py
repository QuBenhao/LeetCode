import solution
from typing import *
from itertools import permutations


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.permute(test_input)

    def permute(self, nums: List[int]) -> List[List[int]]:
        return [list(p) for p in permutations(nums)]
