from itertools import accumulate

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.pivotIndex(test_input)

    def pivotIndex(self, nums: List[int]) -> int:
        pre_sum = [0] + list(accumulate(nums))
        for i, num in enumerate(nums):
            if pre_sum[i] == pre_sum[-1] - pre_sum[i + 1]:
                return i
        return -1
