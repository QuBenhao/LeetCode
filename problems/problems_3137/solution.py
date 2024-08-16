import solution
from typing import *
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumOperationsToMakeKPeriodic(*test_input)

    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        return len(word) // k - max(Counter(word[i:i + k] for i in range(0, len(word), k)).values())
