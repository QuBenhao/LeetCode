import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isGood(test_input)

    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        counts = [0] * (n + 1)
        for num in nums:
            if num > n:
                return False
            counts[num] += 1
            if counts[num] > (2 if num == n else 1):
                return False
        return True
