import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numOfSubsequences(test_input)

    def numOfSubsequences(self, s: str) -> int:
        ans, max_add = 0, 0
        n = len(s)
        suf_t = [0] * (n + 1)
        suf_c = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf_t[i] = suf_t[i + 1] + (s[i] == 'T')
            suf_c[i] = suf_c[i + 1] + (suf_t[i] if s[i] == 'C' else 0)
        pre_l = 0
        pre_c = 0
        for i, c in enumerate(s):
            if c == 'L':
                pre_l += 1
                ans += suf_c[i + 1]
            elif c == 'C':
                pre_c += pre_l
            max_add = max(max_add, suf_c[i], pre_l * suf_t[i], pre_c)
        return ans + max_add
