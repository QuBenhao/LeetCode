import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getKth(*test_input)

    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power(x):
            if x == 1:
                return 0
            if x % 2:
                return power(3 * x + 1) + 1
            return power(x // 2) + 1

        power_map = {1: 0}
        for i in range(lo, hi + 1):
            power_map[i] = power(i)

        return sorted(range(lo, hi + 1), key=lambda x: (power_map[x], x))[k - 1]
