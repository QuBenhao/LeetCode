from itertools import pairwise

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isSubstringPresent(test_input)

    def isSubstringPresent(self, s: str) -> bool:
        visit = set()
        for a, b in pairwise(s):
            visit.add(a + b)
            if b + a in visit:
                return True
        return False
