import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countSquares(test_input)

    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    dp[i+1][j+1] = min(dp[i][j], dp[i][j+1], dp[i+1][j]) + 1
                    ans += dp[i+1][j+1]
        return ans
