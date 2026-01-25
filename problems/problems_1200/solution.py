from itertools import pairwise
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumAbsDifference(test_input)

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans, diff = [], inf
        for a, b in pairwise(sorted(arr)):
            if (d := abs(a - b)) < diff:
                ans = [[a, b]]
                diff = d
            elif d == diff:
                ans.append([a, b])
        return ans
