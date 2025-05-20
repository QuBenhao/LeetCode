from itertools import accumulate

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isZeroArray(*test_input)

    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        for l, r in queries:
            diff[l] += 1
            diff[r + 1] -= 1
        return all(d >= num for d, num in zip(accumulate(diff), nums) if num > 0)
