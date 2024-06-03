import solution
from typing import *
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findTheDifference(*test_input)

    def findTheDifference(self, s: str, t: str) -> str:
        cs, ct = Counter(s), Counter(t)
        for k, v in (ct - cs).items():
            if v != 0:
                return k
        return ""
