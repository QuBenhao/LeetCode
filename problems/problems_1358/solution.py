import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfSubstrings(test_input)

    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [n] * 3
        ans = 0
        for i, c in enumerate(s):
            dp[ord(c) - ord('a')] = i
            if max(dp) < n:
                ans += min(dp) + 1
        return ans
