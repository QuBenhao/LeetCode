import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.subStrHash(*test_input)

    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def f(ch):
            return ord(ch) - ord("a") + 1
        S = sum(f(ch) * power ** mi for mi, ch in enumerate(s[:k]))
        if S % modulo == hashValue: return s[:k]
        for i in range(k, len(s)):
            S = (S - f(s[i-k])) // power + f(s[i]) * power ** (k-1)
            if S % modulo == hashValue:
                return s[i-k+1:i+1]