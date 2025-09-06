from functools import cache
from typing import *

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minOperations(test_input)

    def minOperations(self, queries: List[List[int]]) -> int:
        def helper(s, m):
            # 1953
            return s - m + 1 if m > s - m else (s + 1) // 2

        @cache
        def pre_sum(num: int):
            if num == 0:
                return 0
            b = (num.bit_length() + 1) // 2
            return pre_sum(4 ** (b - 1) - 1) + b * (num + 1 - 4 ** (b - 1))

        ans = 0
        for l, r in queries:
            # log4 N = log2 N / log2 4 = log2 N / 2
            # 1, 2, 3 -> 1
            # 4, 5, 6, ..., 15 -> 2
            # 16, 17, 18, ..., 63 -> 3
            mx = (r.bit_length() + 1) // 2
            sm = pre_sum(r) - pre_sum(l - 1)
            ans += helper(sm, mx)

        return ans
