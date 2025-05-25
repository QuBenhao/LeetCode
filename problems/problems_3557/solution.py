from bisect import bisect_left
from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxSubstrings(test_input)

    def maxSubstrings(self, word: str) -> int:
        idx_map = defaultdict(list)
        for i, c in enumerate(word):
            idx_map[c].append(i)
        n = len(word)
        dp = [0] * (n + 1)
        for i, c in enumerate(word):
            idx = bisect_left(idx_map[c], max(i-1,0))
            while idx >= 0 and i - idx_map[c][idx] < 3:
                idx -= 1
            if idx >= 0 and i - idx_map[c][idx] >= 3:
                dp[i + 1] = max(dp[i], dp[idx_map[c][idx]] + 1)
            else:
                dp[i + 1] = dp[i]
        return dp[n]
