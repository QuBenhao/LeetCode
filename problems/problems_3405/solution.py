from math import comb
import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countGoodArrays(*test_input)

    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        # The first element has m choices; each equal adjacent element has 1 choice and each unequal one has m-1 choices, giving k factors of 1 and n-k-1 factors of m-1
        # Choose k of the n-1 positions for factors of 1; the remaining positions contribute m-1
        mod = 10**9 + 7
        return (((m * pow(m-1, n-k-1, mod)) % mod) * comb(n-1, k)) % mod
