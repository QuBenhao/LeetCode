from collections import defaultdict
from heapq import nlargest

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxSumDistinctTriplet(*test_input)

    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        mp = defaultdict(int)
        for a, b in zip(x, y):
            mp[a] = max(mp[a], b)
        if len(mp) < 3:
            return -1
        return sum(nlargest(3, mp.values()))
