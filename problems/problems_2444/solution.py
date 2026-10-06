import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countSubarrays(*test_input)

    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # Find the left and right limits within each interval, splitting intervals at invalid values
        ans = 0
        min_left, max_left = -1, -1
        invalid = -1
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                invalid = i
            if num == minK:
                min_left = i
            if num == maxK:
                max_left = i
            # With right endpoint i, the rightmost left endpoint must include minK and maxK; the leftmost must be to the right of invalid
            ans += max(0, min(min_left, max_left) - invalid)
        return ans
