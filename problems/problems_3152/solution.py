import solution
from typing import *
from itertools import pairwise


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isArraySpecial(*test_input)

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        pre_sum = [0] * n
        for i, (a, b) in enumerate(pairwise(nums)):
            pre_sum[i + 1] = pre_sum[i] + (a & 1 != b & 1)
        return [pre_sum[b] - pre_sum[a] == b - a for a, b in queries]
