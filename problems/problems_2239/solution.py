from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findClosestNumber(test_input)

    def findClosestNumber(self, nums: List[int]) -> int:
        ans = inf
        for num in nums:
            d = abs(num)
            if d < abs(ans):
                ans = num
            elif d == abs(ans):
                ans = max(ans, num)
        return ans
