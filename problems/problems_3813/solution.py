import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.vowelConsonantScore(test_input)

    def vowelConsonantScore(self, s: str) -> int:
        v = c = 0
        for ch in s:
            if not ch.isalpha():
                continue
            if ch in VOWELS:
                v += 1
            else:
                c += 1
        return c if not c else v // c

VOWELS = "aeiou"
