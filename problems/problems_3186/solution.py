import solution
from collections import Counter
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumTotalDamage(test_input)

    def maximumTotalDamage(self, power: List[int]) -> int:
        counts = Counter(power)
        n = len(counts)
        dp = [0] * (n + 1)
        keys = list(sorted(counts.keys()))
        j = 0
        for i in range(n):
            cur = keys[i]
            while keys[j] < cur - 2:
                j += 1
            dp[i + 1] = max(dp[i], dp[j] + cur * counts[cur])
        return dp[n]
