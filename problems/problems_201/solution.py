import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.rangeBitwiseAnd(*test_input)

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = 0
        for i in range(31, -1, -1):
            cur = 1 << i
            l, r = left & cur, right & cur
            if r > 0 and l == 0:
                return ans
            if r > 0 and l > 0:
                ans |= cur
        return ans
