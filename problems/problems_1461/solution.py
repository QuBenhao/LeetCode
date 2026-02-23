import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.hasAllCodes(*test_input)

    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        target = 1 << k
        if n < target + k - 1:
            return False
        st = set()
        cur = 0
        for i in range(k):
            cur = cur << 1 | ord(s[i]) - ord('0')
        full = target - 1
        st.add(cur)
        for i in range(k, n):
            cur = ((cur << 1) & full) | ord(s[i]) - ord('0')
            st.add(cur)
            if len(st) == target:
                return True
        return False
