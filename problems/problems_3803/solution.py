import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.residuePrefixes(test_input)

    def residuePrefixes(self, s: str) -> int:
        st = set()
        ans = 0
        for i, c in enumerate(s, start=1):
            st.add(c)
            if len(st) == i % 3:
                ans += 1
        return ans
