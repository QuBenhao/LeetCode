from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestBalanced(test_input)

    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            counts = defaultdict(int)
            for j in range(i, n):
                counts[s[j]] += 1
                if all(v == counts[s[j]] for v in counts.values()):
                    ans = max(ans, j - i + 1)
        return ans
