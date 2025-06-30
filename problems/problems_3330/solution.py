from itertools import pairwise

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.possibleStringCount(test_input)

    def possibleStringCount(self, word: str) -> int:
        return 1 + sum(a == b for a, b in pairwise(word))
