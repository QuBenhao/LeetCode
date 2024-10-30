from itertools import pairwise

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getSmallestString(test_input)

    def getSmallestString(self, s: str) -> str:
        for i, (ca, cb) in enumerate(pairwise(s)):
            a, b = int(ca), int(cb)
            if a > b and a % 2 == b % 2:
                return s[:i] + cb + ca + s[i + 2:]
        return s
