import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minMoves(test_input)

    def minMoves(self, nums: List[int]) -> int:
        s, m = 0, nums[0]
        for num in nums:
            if num > m:
                m = num
            s += num
        return m * len(nums) - s
