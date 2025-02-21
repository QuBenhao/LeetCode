from itertools import accumulate

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumWhiteTiles(*test_input)

    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        m = len(floor)
        if numCarpets * carpetLen >= m:
            return 0

        floor = list(map(int, floor))
        f = list(accumulate(floor))
        for i in range(1, numCarpets + 1):
            nf = [0] * m
            for j in range(carpetLen * i, m):
                nf[j] = min(nf[j - 1] + floor[j], f[j - carpetLen])
            f = nf
        return f[-1]
