import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.robotWithString(test_input)

    def robotWithString(self, s: str) -> str:
        n = len(s)
        suf = ['z'] * (n+1)
        for i in range(n - 1, -1, -1):
            suf[i] = min(suf[i + 1], s[i])

        ans = []
        st = []
        for i, c in enumerate(s):
            st.append(c)
            while st and st[-1] <= suf[i+1]:
                ans.append(st.pop())
        return ''.join(ans)
