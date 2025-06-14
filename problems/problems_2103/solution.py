from itertools import pairwise

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countPoints(test_input)

    def countPoints(self, rings: str) -> int:
        explored = [0] * 10
        for c, i in pairwise(rings):
            explored[int(i)] |= 1 << "RGB".index(c)
        return sum(e == (1 << 3) - 1 for e in explored)
