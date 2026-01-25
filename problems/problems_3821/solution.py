from bisect import bisect_left
from math import comb

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.nthSmallest(*test_input)

    def nthSmallest(self, n: int, k: int) -> int:
        # last = 0
        # for i in range(k - 1, 50):
        #     # 二进制第i位, 共有i + 1位可以填1, 从中选k个的取法
        #     cur = comb(i + 1, k)
        #     if cur == n:
        #         return sum(1 << j for j in range(i, i - k, -1))
        #     if cur > n:
        #         return (1 << i) | self.nthSmallest(n - last, k - 1)
        #     last = cur
        # return 0

        ans = 0
        while n > 0:
            # idx 对应 二进制 第idx-1位
            idx = bisect_left(COMBINATIONS[k], n)
            if COMBINATIONS[k][idx] > n:
                ans |= 1 << (idx - 1)
                idx -= 1
            else:
                ans |= sum(1 << j for j in range(idx - 1, idx - 1 - k, -1))
            n -= COMBINATIONS[k][idx]
            k -= 1
        return ans

COMBINATIONS = [[0] * 51 for _ in range(51)]
for _i in range(51):
    COMBINATIONS[0][_i] = 1
    for _j in range(1, _i + 1):
        COMBINATIONS[_j][_i] = COMBINATIONS[_j][_i - 1] + COMBINATIONS[_j - 1][_i - 1]
