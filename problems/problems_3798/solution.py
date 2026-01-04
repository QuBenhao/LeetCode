import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.largestEven(test_input)

    def largestEven(self, s: str) -> str:
        idx = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '2':
                idx = i + 1
                break
        return s[:idx]
