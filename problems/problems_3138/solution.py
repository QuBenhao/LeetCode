import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minAnagramLength(test_input)

    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        for k in range(1, n // 2 + 1):
            if n % k:
                continue
            t = sorted(s[:k])
            if all(sorted(s[i - k: i]) == t for i in range(k * 2, n + 1, k)):
                return k
        return n
