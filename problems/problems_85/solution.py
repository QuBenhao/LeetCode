import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximalRectangle(test_input)

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ans = 0
        n = len(matrix[0])
        dp = [0] * n
        for row in matrix:
            stack = [-1]
            for j in range(n + 1):
                v = -1
                if j < n:
                    dp[j] = 0 if row[j] == '0' else dp[j] + 1
                    v = dp[j]
                while len(stack) > 1 and dp[stack[-1]] >= v:
                    i = stack.pop()
                    left = stack[-1]
                    ans = max(ans, dp[i] * (j - left - 1))
                stack.append(j)
        return ans
