import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfPoints(test_input)

    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        ans, cur = 0, nums[0][0] - 1
        for left, right in nums:
            if left > cur:
                ans += right - left + 1
                cur = right
            elif right > cur:
                ans += right - cur
                cur = right
        return ans
