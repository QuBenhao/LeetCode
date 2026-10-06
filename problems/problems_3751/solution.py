from functools import cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.totalWaviness(*test_input)

    # Compute the sum of waviness values of integers in [1, n]
    def calc(self, n: int) -> int:
        ans = 0

        # Split the integer into five parts: prefix | l | m | r | suffix
        # Enumerate the positions of (l, m, r) from low to high and compute their contribution to the answer
        pow10 = 1
        while n >= pow10 * 100:
            max_prefix = n // (pow10 * 1000)
            n2 = n // pow10
            L = n2 // 100 % 10
            M = n2 // 10 % 10
            R = n2 % 10

            # 1. When prefix < max_prefix, the lower digits are unrestricted
            # But prefix=0 and l=0 is invalid and must be subtracted
            cnt = max_prefix * 570 - 45  # Do not multiply by pow10 yet

            # 2. prefix = max_prefix and l < L
            cnt += (121 + L * 15 - L * L) * L // 3

            # 3. prefix = max_prefix and l = L and m < M
            cnt += (L + M) * max(M - L - 1, 0) // 2  # Peak
            cnt += (19 - min(L, M)) * min(L, M) // 2  # Valley

            # 4. prefix = max_prefix and l = L and m = M and r < R
            if L < M:  # Can only be a peak
                cnt += min(M, R)
            elif L > M:  # Can only be a valley
                cnt += max(R - M - 1, 0)

            # In the cases above, suffix is unrestricted, giving pow10 choices
            ans += cnt * pow10

            # 5. prefix = max_prefix and l = L and m = M and r = R
            if (L - M) * (M - R) < 0:  # Peak or valley
                max_suffix = n % pow10
                ans += max_suffix + 1  # suffix can be any integer in [0, max_suffix]

            pow10 *= 10

        return ans

    def totalWaviness(self, num1: int, num2: int) -> int:
        return self.calc(num2) - self.calc(num1 - 1)

    # def totalWaviness(self, num1: int, num2: int) -> int:
    #     # Digit DP: compute the sum of waviness values of all numbers in [num1, num2]
    #     # Use a difference: f(num2) - f(num1 - 1)
    #
    #     def calc(n: int) -> int:
    #         """Compute the sum of waviness values of all numbers in [1, n]"""
    #         if n <= 0:
    #             return 0
    #         s = list(map(int, str(n)))
    #
    #         @cache
    #         def dfs(i: int, prev: int, pre_prev: int, cnt: int,
    #                 limit: bool, is_num: bool) -> int:
    #             """
    #             i: current digit position
    #             prev: previous significant digit (-1 means not started)
    #             pre_prev: significant digit before prev (-1 means absent)
    #             cnt: accumulated waviness
    #             limit: whether the upper bound applies
    #             is_num: whether digit placement has started
    #             """
    #             if i == len(s):
    #                 return cnt
    #
    #             res = 0
    #             hi = s[i] if limit else 9
    #
    #             # Skip this digit (skip/leading zero)
    #             if not is_num:
    #                 res += dfs(i + 1, -1, -1, 0, False, False)
    #
    #             # Place a digit
    #             start = 1 if not is_num else 0
    #             for d in range(start, hi + 1):
    #                 new_cnt = cnt
    #                 # Check whether prev is a peak or valley
    #                 if prev != -1 and pre_prev != -1:
    #                     if pre_prev < prev > d:  # Peak
    #                         new_cnt += 1
    #                     elif pre_prev > prev < d:  # Valley
    #                         new_cnt += 1
    #
    #                 res += dfs(i + 1, d, prev, new_cnt, limit and d == hi, True)
    #
    #             return res
    #
    #         return dfs(0, -1, -1, 0, True, False)
    #
    #     return calc(num2) - calc(num1 - 1)
