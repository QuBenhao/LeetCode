import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxProduct(test_input)

    def maxProduct(self, n: int) -> int:
        mx, sub_mx = 0, 0
        while n:
            cur = n % 10
            n //= 10
            if cur > mx:
                sub_mx = mx
                mx = cur
            elif cur > sub_mx:
                sub_mx = cur
        return mx * sub_mx
