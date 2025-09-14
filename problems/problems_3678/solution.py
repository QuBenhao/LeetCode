import math

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.smallestAbsent(test_input)

    def smallestAbsent(self, nums: List[int]) -> int:
        s = sum(nums)
        st = set(nums)
        n = len(nums)
        avg = math.ceil((s + 1) / n)
        for i in range(max(1, avg), max(nums) + 2):
            if i not in st:
                return i
        return 1
