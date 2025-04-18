import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getFinalState(*test_input)

    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            mn = min(nums)
            nums[nums.index(mn)] *= multiplier
        return nums
