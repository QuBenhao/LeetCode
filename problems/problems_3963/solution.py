import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.createGrid(*test_input)

    def createGrid(self, m: int, n: int) -> list[str]:
        ans = [['#'] * n for _ in range(m)]
        for i in range(m):
            ans[i][n - 1] = '.'
        for j in range(n):
            ans[0][j] = '.'
        return ["".join(row) for row in ans]
