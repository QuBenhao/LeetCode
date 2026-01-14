from itertools import pairwise

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximizeSquareHoleArea(*test_input)

    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        max_h = cur_h = 1
        max_v = cur_v = 1
        for a, b in pairwise(hBars):
            if b == a + 1:
                cur_h += 1
            else:
                cur_h = 1
            max_h = max(max_h, cur_h)
        for a, b in pairwise(vBars):
            if b == a + 1:
                cur_v += 1
            else:
                cur_v = 1
            max_v = max(max_v, cur_v)
        return (min(max_h, max_v) + 1) ** 2
