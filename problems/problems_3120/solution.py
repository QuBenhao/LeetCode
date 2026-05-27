import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfSpecialChars(test_input)

    def numberOfSpecialChars(self, word: str) -> int:
        check = [0] * 26
        for c in word:
            if c.isupper():
                check[ord(c) - ord('A')] |= 2
            else:
                check[ord(c) - ord('a')] |= 1
        return check.count(3)
