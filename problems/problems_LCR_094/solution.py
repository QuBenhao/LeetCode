import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minCut(test_input)

    def minCut(self, s: str) -> int:
        n = len(s)
        # 预处理回文串
        is_palindrome = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or is_palindrome[i + 1][j - 1]):
                    is_palindrome[i][j] = True

        # 动态规划
        dp = [0x3f3f3f3f] * n
        for i in range(n):
            if is_palindrome[0][i]:
                dp[i] = 0
            else:
                for j in range(i):
                    if is_palindrome[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]
