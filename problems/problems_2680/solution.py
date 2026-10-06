import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumOr(*test_input)

    def maximumOr(self, nums: List[int], k: int) -> int:
        all_or = fixed = 0
        for x in nums:
            # If all_or and x share set bits before computing all_or |= x,
            # multiple nums[i] values have 1s at those bit positions
            fixed |= all_or & x  # Record the shared set bits in fixed
            all_or |= x  # OR of all numbers
        return max((all_or ^ x) | fixed | (x << k) for x in nums)
