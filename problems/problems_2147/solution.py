import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfWays(test_input)

    def numberOfWays(self, corridor: str) -> int:
        sp = corridor.split('S')
        n = len(sp)
        if n % 2 != 1 or n == 1:
            return 0
        ans = 1
        for i in range(2, n - 2, 2):
            ans = ans * (len(sp[i]) + 1) % MOD
        return ans

MOD = 10**9+7
