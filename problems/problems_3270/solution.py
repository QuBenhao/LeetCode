import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.generateKey(*test_input)

    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        ans = 0
        for i in range(4):
            cur = 10 ** i
            ans += min(num1 % (cur * 10) // cur, num2 % (cur * 10) // cur, num3 % (cur * 10) // cur) * cur
        return ans
