from itertools import pairwise

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minCost(*test_input)

    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        for i, (a, b) in enumerate(pairwise(colors)):
            if a == b:
                ans += min(neededTime[i], neededTime[i + 1])
                neededTime[i + 1] = max(neededTime[i], neededTime[i + 1])
        return ans
