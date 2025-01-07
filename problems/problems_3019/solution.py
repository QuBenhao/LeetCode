from itertools import pairwise

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countKeyChanges(test_input)

    def countKeyChanges(self, s: str) -> int:
        ans = 0
        for a, b in pairwise(s):
            ans += b.lower() != a.lower()
        return ans
