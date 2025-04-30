import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.knightProbability(*test_input)

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dirs = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]
        dp = [[[1.0, 0.0] for _ in range(n)] for _ in range(n)]
        for p in range(1, k+1):
            for i in range(n):
                for j in range(n):
                    dp[i][j][p%2]=0
                    for dx, dy in dirs:
                        if (nx := i + dx) < 0 or nx >= n or (ny := j + dy) < 0 or ny >= n:
                            continue
                        dp[i][j][p%2] += dp[nx][ny][(p+1)%2] / 8
        return dp[row][column][k%2]

