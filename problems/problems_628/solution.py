import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumProduct(test_input)

    def maximumProduct(self, nums: List[int]) -> int:
        max1 = max2 = max3 = -1001
        min1 = min2 = 1001
        for x in nums:
            if x > max1:
                max1, max2, max3 = x, max1, max2
            elif x > max2:
                max2, max3 = x, max2
            elif x > max3:
                max3 = x
            if x < min1:
                min1, min2 = x, min1
            elif x < min2:
                min2 = x
        return max(max1 * max2 * max3, min1 * min2 * max1)

