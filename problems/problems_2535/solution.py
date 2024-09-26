import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.differenceOfSum(test_input)

    def differenceOfSum(self, nums: List[int]) -> int:
        s1, s2 = 0, 0
        for num in nums:
            s1 += num
            while num:
                s2 += num % 10
                num //= 10
        return abs(s1 - s2)
