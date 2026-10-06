import solution
from typing import *
from functools import cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countSpecialNumbers(test_input)

    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)
        @cache  # Cache decorator to avoid recomputing dfs results (memoization)
        def dfs(i: int, mask: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s):
                return 1 if is_num else 0  # is_num being True means a valid number has been formed
            res = 0
            if not is_num:  # The current digit can be skipped
                res = dfs(i + 1, mask, False, False)
            # If no digit has been placed, start at 1 to avoid leading zeros
            low = 0 if is_num else 1
            # If all previous digits match n, this digit can be at most s[i] (otherwise the number would exceed n)
            up = int(s[i]) if is_limit else 9
            for d in range(low, up + 1):  # Enumerate the digit d to place
                if mask >> d & 1 == 0:  # If d is absent from mask, it has not been used before
                    res += dfs(i + 1, mask | (1 << d), is_limit and d == up, True)
            return res
        return dfs(0, 0, True, False)


