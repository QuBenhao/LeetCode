import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countPermutations(test_input)

    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        if any(complexity[i] <= complexity[0] for i in range(1, n)):
            return 0
        MOD = 10**9 + 7
        ans = 1
        for i in range(2, n):
            ans = (ans * i) % MOD
        return ans

