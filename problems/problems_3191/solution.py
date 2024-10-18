import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minOperations(test_input)

    def minOperations(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(n - 2):
            if nums[i]:
                continue
            ans += 1
            nums[i + 1] ^= 1
            nums[i + 2] ^= 1
        return ans if nums[-2] and nums[-1] else -1
