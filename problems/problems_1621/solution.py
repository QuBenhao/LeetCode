from math import comb

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfSets(*test_input)

    def numberOfSets(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        return comb(n + k - 1, 2 * k) % mod

        # # dp[j]: 前 i 个点中选 j 条线段的方案数（滚动 i）
        # # pre[j]: sum(dp_t[j] for t in 1..i)，即各层第 j 列的前缀和
        # dp = [1] + [0] * k
        # pre = [0] * (k + 1)
        # for _ in range(n):
        #     cur = [1] + [0] * k
        #     for j in range(k, 0, -1):
        #         # 第 i 个点不使用 -> dp[j]；作为最后一条线段右端点 -> pre[j-1]
        #         cur[j] = (dp[j] + pre[j - 1]) % mod
        #     for j in range(k + 1):
        #         pre[j] = (pre[j] + cur[j]) % mod
        #     dp = cur
        # return dp[k]
