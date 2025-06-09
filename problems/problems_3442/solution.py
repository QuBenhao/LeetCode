import solution
from collections import Counter
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxDifference(test_input)

    def maxDifference(self, s: str) -> int:
        counter = Counter(s)
        min_even, max_odd = len(s), 0
        for v in counter.values():
            if v % 2 == 0:
                min_even = min(min_even, v)
            else:
                max_odd = max(max_odd, v)
        return max_odd - min_even
