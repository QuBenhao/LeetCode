import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.removeKdigits(*test_input)

    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for c in num:
            while k and st and st[-1] > c:
                st.pop()
                k -= 1
            st.append(c)
        if k:
            st = st[:-k]
        ans = ''.join(st).lstrip('0')
        return ans if ans else '0'
