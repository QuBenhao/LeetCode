from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minCost(*test_input)

    def minCost(self, s: str, cost: List[int]) -> int:
        counts = defaultdict(int)
        sm = 0
        for c, ct in zip(s, cost):
            counts[c] += ct
            sm += ct
        return sm - max(counts.values())
