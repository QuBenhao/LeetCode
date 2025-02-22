from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.similarPairs(test_input)

    def similarPairs(self, words: List[str]) -> int:
        counter = defaultdict(int)
        ans = 0
        for word in words:
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            ans += counter[mask]
            counter[mask] += 1
        return ans
