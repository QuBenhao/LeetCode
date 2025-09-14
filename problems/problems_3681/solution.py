import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxXorSubsequences(test_input)

    def maxXorSubsequences(self, nums: List[int]) -> int:
        if not nums:
            return 0
        base = [0] * 32

        for x in nums:
            for i in range(31, -1, -1):
                if (x >> i) & 1:
                    if base[i]:
                        x ^= base[i]
                    else:
                        base[i] = x
                        break

        res = 0
        for i in range(31, -1, -1):
            if base[i] != 0 and (res >> i) & 1 == 0:
                res ^= base[i]

        return res
