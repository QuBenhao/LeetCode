import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.myPow(*test_input)

    def myPow(self, x: float, n: int) -> float:
        # 矩阵快速幂
        if x == 0.0:
            return 0.0
        if n < 0:
            x, n = 1 / x, -n
        ans = 1.0
        while n:
            if n & 1:
                ans *= x
            x *= x
            n >>= 1
        return ans
