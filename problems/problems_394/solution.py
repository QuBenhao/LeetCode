import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.decodeString(test_input)

    def decodeString(self, s: str) -> str:
        stack, res, times = [], "", 0
        for c in s:
            if c == '[':
                stack.append((res, times))
                res, times = "", 0
            elif c == ']':
                last, t = stack.pop()
                res = last + t * res
            elif c.isdigit():
                times = times * 10 + int(c)
            else:
                res += c
        return res
