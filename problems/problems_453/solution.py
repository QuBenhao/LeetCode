import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minMoves(test_input)

    def minMoves(self, nums: List[int]) -> int:
        n = len(nums)
        s, m = 0, nums[0]
        for num in nums:
            s += num
            if num < m:
                m = num
        return s - m * n

