import solution
from typing import *
import itertools


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestContinuousSubstring(test_input)

    def longestContinuousSubstring(self, s: str) -> int:
        ans, cur = 1, 1
        for a, b in itertools.pairwise(s):
            if ord(b) - ord(a) == 1:
                cur += 1
                ans = max(ans, cur)
            else:
                cur = 1
        return ans
