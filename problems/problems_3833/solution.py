import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.dominantIndices(test_input)

    def dominantIndices(self, nums: List[int]) -> int:
        s = sum(nums)
        ans, cur, n = 0, 0, len(nums)
        for i, num in enumerate(nums):
            cur += num
            if i < n - 1 and num * (n - 1 - i) > s - cur:
                ans += 1
        return ans
