import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findPermutationDifference(*test_input)

    def findPermutationDifference(self, s: str, t: str) -> int:
        idx_s = {c: i for i, c in enumerate(s)}
        idx_t = {c: i for i, c in enumerate(t)}
        return sum(abs(idx_s[c] - idx_t[c]) for c in s)
