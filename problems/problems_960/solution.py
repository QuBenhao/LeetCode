import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minDeletionSize(test_input)

    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs[0])
        f = [0] * m
        for i in range(m):
            for j in range(i):
                if f[j] > f[i] and all(s[j] <= s[i] for s in strs):
                    f[i] = f[j]
            f[i] += 1
        return m - max(f)
