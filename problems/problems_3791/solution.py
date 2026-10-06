from functools import cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countBalanced(*test_input)

    def countBalanced(self, low: int, high: int) -> int:
        def digitDP(low: int, high: int, target: int) -> int:
            low_s = list(map(int, str(low)))  # Avoid frequent int() calls in dfs
            high_s = list(map(int, str(high)))
            n = len(high_s)
            diff_lh = n - len(low_s)

            @cache
            def dfs(i: int, cnt0: int, limit_low: bool, limit_high: bool) -> int:
                # if cnt0 > target:
                #     return 0  # Invalid
                if i == n:
                    return 1 if cnt0 == 0 else 0

                lo = low_s[i - diff_lh] if limit_low and i >= diff_lh else 0
                hi = high_s[i] if limit_high else 9

                res = 0
                start = lo

                # limit_low and i determine whether a digit can be skipped; no is_num parameter is needed
                # Remove this if block if leading zeros do not affect the answer
                if limit_low and i < diff_lh:
                    # Skip this digit; the upper bound no longer applies
                    res = dfs(i + 1, 0, True, False)
                    start = 1

                for d in range(start, hi + 1):
                    res += dfs(i + 1,
                               cnt0 + (d if i % 2 == 0 else -d),  # Count zeros
                               limit_low and d == lo,
                               limit_high and d == hi)

                # res %= MOD
                return res

            return dfs(0, 0, True, True)

        return digitDP(low, high, 0)

