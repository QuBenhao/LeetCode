import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxSum(test_input)

    def maxSum(self, nums: List[int]) -> int:
        return sum(s) if (s := set(num for num in nums if num > 0)) else max(nums)
