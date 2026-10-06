from math import comb

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfSets(*test_input)

    def numberOfSets(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        return comb(n + k - 1, 2 * k) % mod

        # # dp[j]: ways to choose j segments among the first i points (rolling over i)
        # # pre[j]: sum(dp_t[j] for t in 1..i), the prefix sum of column j across layers
        # dp = [1] + [0] * k
        # pre = [0] * (k + 1)
        # for _ in range(n):
        #     cur = [1] + [0] * k
        #     for j in range(k, 0, -1):
        #         # Leave point i unused -> dp[j]; use it as the last segment's right endpoint -> pre[j-1]
        #         cur[j] = (dp[j] + pre[j - 1]) % mod
        #     for j in range(k + 1):
        #         pre[j] = (pre[j] + cur[j]) % mod
        #     dp = cur
        # return dp[k]
