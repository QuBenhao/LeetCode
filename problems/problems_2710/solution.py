import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.removeTrailingZeros(test_input)

    def removeTrailingZeros(self, num: str) -> str:
        idx = len(num) - 1
        while idx >= 0 and num[idx] == '0':
            idx -= 1
        return num[:idx + 1]
