import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isValid(test_input)

    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        has_vowel, has_consonant = False, False
        for c in word:
            if not c.isalnum():
                return False
            if c.lower() in "aeiou":
                has_vowel = True
            elif c.isalpha():
                has_consonant = True
        return has_vowel and has_consonant
