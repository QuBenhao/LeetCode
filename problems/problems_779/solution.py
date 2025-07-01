from functools import cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.kthGrammar(*test_input)

    @cache
    def kthGrammar(self, n: int, k: int) -> int:
        return (1 - self.kthGrammar(n - 1, ((k + 1) >> 1))) ^ (k & 1) if n > 1 else 0
