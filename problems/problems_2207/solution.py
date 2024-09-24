import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumSubsequenceCount(*test_input)

    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        ans = 0
        p0 = p1 = 0
        for c in text:
            if c == pattern[1]:
                ans += p0
                p1 += 1
            if c == pattern[0]:
                p0 += 1
        return ans + max(p0, p1)
