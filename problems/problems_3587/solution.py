from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minSwaps(test_input)

    def minSwaps(self, nums: List[int]) -> int:
        vals = [[], []]
        for i, num in enumerate(nums):
            vals[num % 2].append(i)

        def min_swap(start: int) -> int:
            cnt = 0
            for i, j in zip(vals[start], range(0, len(nums), 2)):
                cnt += abs(i - j)
            return cnt

        if abs(len(vals[0]) - len(vals[1])) > 1:
            return -1
        ans = inf
        if len(vals[0]) >= len(vals[1]):
            ans = min(ans, min_swap(0))
        if len(vals[1]) >= len(vals[0]):
            ans = min(ans, min_swap(1))
        return ans
