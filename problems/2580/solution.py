import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countWays(test_input)

    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        ans, cur = 0, -1
        for a, b in ranges:
            if a > cur:
                ans += 1
            cur = max(cur, b)
        return pow(2, ans, int(1e9) + 7)
