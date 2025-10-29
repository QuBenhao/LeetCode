from itertools import pairwise

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minNumberOperations(test_input)

    def minNumberOperations(self, target: List[int]) -> int:
        ans = target[0]
        for a, b in pairwise(target):
            ans += max(0, b - a)
        return ans
