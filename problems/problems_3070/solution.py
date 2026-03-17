import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countSubmatrices(*test_input)

    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        ans = 0
        sums = [0] * len(grid[0])
        for row in grid:
            pre = 0
            for j, val in enumerate(row):
                pre += val
                sums[j] += pre
                if sums[j] <= k:
                    ans += 1
        return ans
