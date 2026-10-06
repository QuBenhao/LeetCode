from functools import cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxPartitionsAfterOperations(*test_input)

    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        @cache
        def dfs(i, st, w):
            """
            i: current index
            st: set of characters encountered so far (bitmask)
            w: whether the one-time replacement with any character is available (true: still available)
            """
            if i == len(s):
                return 1
            ans = 0
            c = ord(s[i]) - ord('a')
            for a in (range(26) if w else [c]):
                st2 = st | 1 << a
                if st2.bit_count() <= k:
                    ans = max(ans, dfs(i + 1, st2, w - (a != c)))
                else:
                    ans = max(ans, 1 + dfs(i + 1, 1 << a, w - (a != c)))
            return ans

        return dfs(0, 0, 1)
