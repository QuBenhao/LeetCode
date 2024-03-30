import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.wordPattern(*test_input)

    def wordPattern(self, pattern: str, s: str) -> bool:
        sp = s.split(" ")
        if len(sp) != len(pattern):
            return False
        mp1, mp2 = dict(), dict()
        for c, st in zip(pattern, sp):
            if c in mp1:
                if mp1[c] != st:
                    return False
            else:
                mp1[c] = st
            if st in mp2:
                if mp2[st] != c:
                    return False
            else:
                mp2[st] = c
        return True
