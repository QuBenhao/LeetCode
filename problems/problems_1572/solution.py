import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.diagonalSum(test_input)

    def diagonalSum(self, mat: List[List[int]]) -> int:
        n, ans = len(mat), 0
        for i in range(n):
            ans += mat[i][i] + mat[i][n - 1 - i]
        return ans - mat[n // 2][n // 2] if n % 2 else ans
