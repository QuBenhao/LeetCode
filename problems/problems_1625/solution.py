from math import gcd

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findLexSmallestString(*test_input)

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        res = s
        s = s + s
        g = gcd(b, n)

        def add(t, start):
            original = int(t[start])
            min_val, times = 10, 0
            for i in range(10):
                added = (original + i * a) % 10
                if added < min_val:
                    min_val = added
                    times = i
            t_list = list(t)
            for i in range(start, n, 2):
                t_list[i] = str((int(t_list[i]) + times * a) % 10)
            return ''.join(t_list)

        for i in range(0, n, g):
            t = s[i:i + n]
            t = add(t, 1)
            if b % 2:
                t = add(t, 0)
            if t < res:
                res = t
        return res
