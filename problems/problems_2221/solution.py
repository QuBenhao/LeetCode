import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.triangularSum(test_input)

    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n - 1, 0, -1):
            for j in range(n - 1, n - 1 - i, -1):
                nums[j] = (nums[j] + nums[j - 1]) % 10
        return nums[-1]
