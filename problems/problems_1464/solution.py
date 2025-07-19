import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxProduct(test_input)

    def maxProduct(self, nums: List[int]) -> int:
        mx1, mx2 = 0, 0
        for num in nums:
            if num > mx1:
                mx2 = mx1
                mx1 = num
            elif num > mx2:
                mx2 = num
        return (mx1 - 1) * (mx2 - 1)
