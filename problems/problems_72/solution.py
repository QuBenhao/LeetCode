import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minDistance(*test_input)

    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            dp[i + 1][0] = i + 1
        for j in range(n):
            dp[0][j + 1] = j + 1
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1], dp[i][j]) + 1
        return dp[m][n]
