import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.smallestIndex(test_input)

    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if sum(map(int, str(num))) == i:
                return i
        return -1
