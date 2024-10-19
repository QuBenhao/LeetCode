import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minOperations(test_input)

    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            if ans % 2 == num:
                ans += 1
        return ans
