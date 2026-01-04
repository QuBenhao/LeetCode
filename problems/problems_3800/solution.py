import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumCost(*test_input)

    def minimumCost(self, s: str, t: str, flipCost: int, swapCost: int, crossCost: int) -> int:
        s1 = t1 = 0
        for c1, c2 in zip(s, t):
            if c1 == c2:
                continue
            if c1 == '1':
                s1 += 1
            else:
                t1 += 1
        ans = flipCost * (s1 + t1)
        d = max(s1, t1) - min(s1, t1)
        ans2 = min(s1, t1) * swapCost + min(d * flipCost, d // 2 * (crossCost + swapCost) + d % 2 * flipCost)
        return min(ans2, ans)
