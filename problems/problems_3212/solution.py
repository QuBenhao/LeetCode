import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfSubmatrices(test_input)

    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n = len(grid[0])
        xs, ys = [0] * n, [0] * n
        ans = 0
        for row in grid:
            pre_x, pre_y = 0, 0
            for j, val in enumerate(row):
                if val == "X":
                    pre_x += 1
                if val == "Y":
                    pre_y += 1
                xs[j] += pre_x
                ys[j] += pre_y
                if xs[j] > 0 and xs[j] == ys[j]:
                    ans += 1
        return ans
