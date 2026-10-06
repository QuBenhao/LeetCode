from functools import cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfPowerfulInt(*test_input)

    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        high = list(map(int, str(finish)))  # Avoid repeated int() calls inside dfs
        n = len(high)
        low = list(map(int, str(start).zfill(n)))  # Pad with leading zeros to match the length of high
        diff = n - len(s)

        @cache
        def dfs(i: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1

            # Enumerate the i-th digit from lo to hi
            # Apply any other digit constraints only in the for loop below; do not change lo or hi
            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else 9

            res = 0
            if i < diff:  # Enumerate the digit to place here
                for d in range(lo, min(hi, limit) + 1):
                    res += dfs(i + 1, limit_low and d == lo, limit_high and d == hi)
            else:  # This digit must be s[i-diff]
                x = int(s[i - diff])
                if lo <= x <= hi:  # The problem guarantees x <= limit, so no check is needed
                    res = dfs(i + 1, limit_low and x == lo, limit_high and x == hi)
            return res

        return dfs(0, True, True)
