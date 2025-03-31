import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.mostPoints(test_input)

    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * (len(questions) + 1)
        n = len(questions)
        for i, (points, brainpower) in enumerate(questions):
            dp[i + 1] = max(dp[i], dp[i + 1])
            nxt = min(i + brainpower + 1, n)
            dp[nxt] = max(dp[nxt], dp[i] + points)
        return dp[-1]
