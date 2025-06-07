import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.clearStars(test_input)

    def clearStars(self, s: str) -> str:
        st = [[] for _ in range(26)]
        mask = 0
        s = list(s)
        for i, c in enumerate(s):
            if c == '*':
                lb = mask & -mask
                stack = st[lb.bit_length() - 1]
                s[stack.pop()] = '*'
                if not stack:
                    mask &= ~lb
            else:
                c = ord(c) - ord('a')
                st[c].append(i)
                mask |= 1 << c
        return ''.join(c for c in s if c != '*')