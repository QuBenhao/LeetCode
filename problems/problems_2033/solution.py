import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minOperations(*test_input)

    def minOperations(self, grid: List[List[int]], x: int) -> int:
        d = grid[0][0] % x
        ks = []
        for row in grid:
            for v in row:
                if v % x != d:
                    return -1
                ks.append((v - grid[0][0]) // x)

        ks.sort()
        mid = ks[len(ks) // 2]
        return sum(abs(k - mid) for k in ks)

