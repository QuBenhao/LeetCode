import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minEatingSpeed(*test_input)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        helper = lambda k: sum((p - 1) // k + 1 for p in piles) <= h

        left, right = 1, max(piles)
        while left < right:
            mid = (left + right - 1) // 2
            if helper(mid):
                right = mid
            else:
                left = mid + 1
        return left
