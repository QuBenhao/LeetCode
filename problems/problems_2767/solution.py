from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumBeautifulSubstrings(test_input)

    def minimumBeautifulSubstrings(self, s: str) -> int:
        def is_five_pow(num: int) -> bool:
            if num == 0:
                return False
            while num % 5 == 0:
                num //= 5
            return num == 1

        n = len(s)
        pre_sum = [0] * (n + 1)
        for i, c in enumerate(map(int, s)):
            pre_sum[i+1] = (pre_sum[i] << 1) + c
        dp = [inf] * (n + 1)
        dp[0] = 0
        for i in range(n):
            for j in range(i+1):
                if s[j] == '0':
                    continue
                cur = pre_sum[i+1] - (pre_sum[j] << (i - j + 1))
                if is_five_pow(cur):
                    dp[i+1] = min(dp[i+1], dp[j] + 1)
        return dp[n] if dp[n] != inf else -1
