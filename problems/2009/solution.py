import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minOperations(test_input)

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        values = sorted(set(nums))
        ans = left = 0
        for i, num in enumerate(values):
            while values[left] < num - n + 1:
                left += 1
            ans = max(ans, i - left + 1)
        return n - ans
