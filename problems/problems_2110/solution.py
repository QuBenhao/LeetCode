from itertools import pairwise
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getDescentPeriods(test_input)

    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = len(prices)
        length = 0
        for a, b in pairwise(prices + [inf]):
            if a - b == 1:
                length = 2 if length == 0 else length + 1
            else:
                ans += length * (length - 1) // 2
                length = 0
        return ans
