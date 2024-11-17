import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.mySqrt(test_input)

    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left, right = 1, x
        while left < right:
            mid = left + (right - left) // 2
            if mid > x // mid:
                right = mid
            else:
                if mid + 1 > x // (mid + 1):
                    return mid
                left = mid + 1
        return left
