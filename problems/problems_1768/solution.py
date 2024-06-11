import solution
from typing import *
from itertools import zip_longest


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.mergeAlternately(*test_input)

    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        for a, b in zip_longest(word1, word2, fillvalue=''):
            ans.append(a)
            ans.append(b)
        return "".join(ans)
