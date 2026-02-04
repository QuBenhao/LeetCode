import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.constructTransformedArray(test_input)

    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [nums[(i + nums[i]) % n] if nums[i] != 0 else 0 for i in range(n)]
