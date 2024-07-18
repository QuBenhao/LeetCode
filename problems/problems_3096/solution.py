import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumLevels(test_input)

    def minimumLevels(self, possible: List[int]) -> int:
        s = sum(p if p > 0 else -1 for p in possible)
        # bob = s - alice
        # alice > bol, alice * 2 > s
        pre = 0
        for i, p in enumerate(possible[:-1]):
            pre += p if p > 0 else -1
            if pre * 2 > s:
                return i + 1
        return -1
