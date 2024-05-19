import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.mySqrt(test_input)

    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left < right:
            mid = (right - left + 1) // 2 + left
            if x // mid < mid:
                right = mid - 1
            else:
                left = mid
        return left
