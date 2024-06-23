import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.detectCapitalUse(test_input)

    def detectCapitalUse(self, word: str) -> bool:
        if word[-1].isupper():
            return word.isupper()
        if word[0].isupper():
            return all(word[i].islower() for i in range(1, len(word)))
        return word.islower()
