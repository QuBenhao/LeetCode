import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sortVowels(test_input)

    def sortVowels(self, s: str) -> str:
        vowels = sorted(filter(lambda c: c in VOWELS, s), key=lambda c: ord(c))
        ans = list(s)
        idx = 0
        for i, c in enumerate(ans):
            if c in VOWELS:
                ans[i] = vowels[idx]
                idx += 1
        return "".join(ans)

VOWELS = "AEIOUaeiou"
