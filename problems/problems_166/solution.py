import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.fractionToDecimal(*test_input)

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)
        a, b = abs(numerator), abs(denominator)
        ans = ("-" if numerator * denominator < 0 else "") + str(a // b) + "."
        cache, i = {}, len(ans)
        while (a := a % b * 10) > 0:
            if a in cache:
                return ans[:cache[a]] + "(" + ans[cache[a]:] + ")"
            ans += str(a//b)
            cache[a] = i
            i += 1
        return ans
