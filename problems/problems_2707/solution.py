import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minExtraChar(*test_input)

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(i):
                if s[j:i] in dictionary:
                    dp[i] = min(dp[i], dp[j])
        return dp[n]
