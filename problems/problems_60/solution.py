from functools import cache

import solution
from typing import *

class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getPermutation(*test_input)

    @cache
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        picks = [i for i in range(1, n + 1)]
        ans = []
        while n > 0:
            d, r = divmod(k, VALS[n - 1])
            k = r
            ans.append(str(picks[d]))
            picks.pop(d)
            n -= 1
        return ''.join(ans)

VALS = [1] * 10
for _i in range(1, 10):
    VALS[_i] = VALS[_i - 1] * _i
