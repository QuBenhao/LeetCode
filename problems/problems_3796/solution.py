from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findMaxVal(*test_input)

    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        nums = [inf] * n
        nums[0] = 0
        for i, r in restrictions:
            nums[i] = r
        for i in range(1, n):
            nums[i] = min(nums[i], nums[i - 1] + diff[i - 1])
        for i in range(n - 2, -1, -1):
            nums[i] = min(nums[i], nums[i + 1] + diff[i])
        return max(nums)
