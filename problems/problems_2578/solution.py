import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.splitNum(test_input)

    def splitNum(self, num: int) -> int:
        nums = []
        while num:
            if r := num % 10:
                nums.append(r)
            num //= 10
        nums.sort()
        a = b = 0
        for v in nums:
            if a <= b:
                a = a * 10 + v
            else:
                b = b * 10 + v
        return a + b
