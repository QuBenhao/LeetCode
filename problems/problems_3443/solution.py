import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxDistance(*test_input)

    def maxDistance(self, s: str, k: int) -> int:
        ans = 0
        k *= 2
        contribute = {'N': (0, 1), 'S': (0, -1), 'E': (1, 1), 'W': (1, -1)}
        counts = [0, 0]
        for i, c in enumerate(s):
            j, c = contribute[c]
            counts[j] += c
            ans = max(ans, min(i+1, abs(counts[0]) + abs(counts[1]) + k))
        return ans
