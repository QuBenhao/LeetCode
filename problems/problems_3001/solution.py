import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minMovesToCaptureTheQueen(*test_input)

    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # m 在 l 和 r 之间（写不写等号都可以）
        def in_between(l: int, m: int, r: int) -> bool:
            return min(l, r) < m < max(l, r)

        # 车直接攻击到皇后 or 象直接攻击到皇后
        if a == e and (c != e or not in_between(b, d, f)) or \
                b == f and (d != f or not in_between(a, c, e)) or \
                c + d == e + f and (a + b != e + f or not in_between(c, a, e)) or \
                c - d == e - f and (a - b != e - f or not in_between(c, a, e)):
            return 1
        return 2
