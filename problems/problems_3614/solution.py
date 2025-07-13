import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.processStr(*test_input)

    def processStr(self, s: str, k: int) -> str:
        length = 0
        n = len(s)
        invalids = set()
        for i, c in enumerate(s):
            if c.isalpha():
                length += 1
            elif c == '#':
                length *= 2
            elif c == '*':
                if length > 0:
                    length -= 1
                else:
                    invalids.add(n - 1 - i)
        if k >= length:
            return '.'
        for i, c in enumerate(s[::-1]):
            if i in invalids:
                continue
            if c.isalpha():
                if k == length - 1:
                    return c
                length -= 1
            elif c == '#':
                if k >= length // 2:
                    k -= length // 2
                length //= 2
            elif c == '%':
                k = length - 1 - k
            else:
                length += 1
        return s[k]
