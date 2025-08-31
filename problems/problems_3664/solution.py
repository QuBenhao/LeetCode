import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.score(*test_input)

    def score(self, cards: List[str], x: str) -> int:
        xx = 0
        x0 = [0] * 10
        x1 = [0] * 10
        for c in cards:
            if c[0] == x and c[1] == x:
                xx += 1
            elif c[0] == x:
                x0[ord(c[1]) - ord('a')] += 1
            elif c[1] == x:
                x1[ord(c[0]) - ord('a')] += 1

        # 1953
        def helper(sm, mx):
            return sm - mx if mx > sm - mx  else sm // 2

        ans = 0
        s0, s1, mx0, mx1 = sum(x0), sum(x1), max(x0), max(x1)
        for i in range(xx + 1):
            ans = max(ans, helper(s0 + i, max(mx0, i)) + helper(s1 + xx - i, max(mx1, xx - i)))
        return ans
