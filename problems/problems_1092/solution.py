import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.shortestCommonSupersequence(*test_input)

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        i, j = m - 1, n - 1
        ans = []
        while i >= 0 or j >= 0:
            if i < 0:
                ans.append(str2[j])
                j -= 1
                continue
            if j < 0:
                ans.append(str1[i])
                i -= 1
                continue
            if str1[i] == str2[j]:
                ans.append(str1[i])
                i -= 1
                j -= 1
                continue
            if dp[i + 1][j] <= dp[i][j + 1]:
                ans.append(str1[i])
                i -= 1
            else:
                ans.append(str2[j])
                j -= 1
        return ''.join(reversed(ans))
