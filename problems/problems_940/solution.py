import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.distinctSubseqII(test_input)

    def distinctSubseqII(self, s: str) -> int:
        mod = 10 ** 9 + 7
        dp = [0] * 26  # dp[c]: the number of distinct subsequences ending in character c
        for ch in s:
            dp[ord(ch) - 97] = (sum(dp) + 1) % mod  # Append to every subsequence, plus ch on its own
        return sum(dp) % mod

