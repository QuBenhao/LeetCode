import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxSumOfSquares(*test_input)

    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if 9 * num < sum:
            return ""
        ans = ""
        for i in range(num):
            if not sum:
                ans += "0" * (num - i)
                break
            v = 9 if sum > 9 else sum
            ans += str(v)
            sum -= v
        return ans
