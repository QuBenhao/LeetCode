import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minBitwiseArray(test_input)

    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        for i, num in enumerate(nums):
            if not (num & 1):
                continue
            j = 0
            while j < num.bit_length():
                if not (num >> j & 1):
                    break
                j += 1
            v = (1 << j) - 1
            ans[i] = (num - v) | v >> 1
        return ans
