import solution
from typing import *
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxNumberOfBalloons(test_input)

    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        return min(count["b"], count["a"], count["l"] // 2, count["o"] // 2, count["n"])
