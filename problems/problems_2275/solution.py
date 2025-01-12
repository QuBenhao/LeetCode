import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.largestCombination(test_input)

    def largestCombination(self, candidates: List[int]) -> int:
        cnt = [0] * 24
        for x in candidates:
            i = 0
            while x:
                cnt[i] += x & 1
                x >>= 1
                i += 1
        return max(cnt)
