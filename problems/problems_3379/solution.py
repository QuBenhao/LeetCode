import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.constructTransformedArray(test_input)

    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        for i in range(n):
            if nums[i] != 0:
                result[i] = nums[(i + nums[i] % n) % n]
            else:
                result[i] = 0
        return result
