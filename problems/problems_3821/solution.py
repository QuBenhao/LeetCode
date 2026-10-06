from bisect import bisect_left
from math import comb

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.nthSmallest(*test_input)

    def nthSmallest(self, n: int, k: int) -> int:
        ## Solution 1
        # last = 0
        # for i in range(k - 1, 50):
        #     # At bit i, there are i + 1 positions available for ones; count the ways to choose k of them
        #     cur = comb(i + 1, k)
        #     if cur == n:
        #         return sum(1 << j for j in range(i, i - k, -1))
        #     if cur > n:
        #         return (1 << i) | self.nthSmallest(n - last, k - 1)
        #     last = cur
        # return 0

        ## Solution 2
        # ans = 0
        # while n > 0:
        #     # idx corresponds to bit idx-1
        #     idx = bisect_left(COMBINATIONS[k], n)
        #     if COMBINATIONS[k][idx] > n:
        #         ans |= 1 << (idx - 1)
        #         idx -= 1
        #     else:
        #         ans |= sum(1 << j for j in range(idx - 1, idx - 1 - k, -1))
        #     n -= COMBINATIONS[k][idx]
        #     k -= 1
        # return ans

        ## Solution 3
        ans = 0
        for i in range(49, -1, -1):
            # If the current bit is not set to 1, do the remaining bits allow at least n choices? If not, this bit must be set
            if COMBINATIONS[k][i] < n:
                ans |= 1 << i
                n -= COMBINATIONS[k][i]
                k -= 1
        return ans


COMBINATIONS = [[0] * 51 for _ in range(51)]
for _i in range(51):
    COMBINATIONS[0][_i] = 1
    for _j in range(1, _i + 1):
        COMBINATIONS[_j][_i] = COMBINATIONS[_j][_i - 1] + COMBINATIONS[_j - 1][_i - 1]
