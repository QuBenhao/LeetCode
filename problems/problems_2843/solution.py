import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countSymmetricIntegers(*test_input)

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high + 1):
            s = str(i)
            if len(s) % 2 == 0:
                n = len(s) // 2
                if sum(map(int, s[:n])) == sum(map(int, s[n:])):
                    ans += 1
        return ans
