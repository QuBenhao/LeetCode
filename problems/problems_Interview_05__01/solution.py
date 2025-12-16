import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.insertBits(*test_input)

    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        for idx in range(i, j + 1):
            if (M >> (idx - i)) & 1:
                N |= 1 << idx
            elif (N >> idx) & 1:
                N ^= 1 << idx
        return N
