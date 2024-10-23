import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countCompleteDayPairs(test_input)

    def countCompleteDayPairs(self, hours: List[int]) -> int:
        hs = [0] * 24
        for h in hours:
            hs[h % 24] += 1
        return sum(hs[i] * hs[24 - i] for i in range(1, 12)) + hs[0] * (hs[0] - 1) // 2 + hs[12] * (hs[12] - 1) // 2

