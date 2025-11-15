import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numSub(test_input)

    def numSub(self, s: str) -> int:
        ans = cur = 0
        for c in s + '0':
            if c == '1':
                cur += 1
            else:
                ans = (ans + (cur + 1) * cur // 2) % MOD
                cur = 0
        return ans

MOD = 10**9 + 7
