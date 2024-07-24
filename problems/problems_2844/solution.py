import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumOperations(test_input)

    def minimumOperations(self, num: str) -> int:
        n = len(num)
        zero = five = False
        for i in range(n - 1, -1, -1):
            c = num[i]
            if (zero and c in "05") or (five and c in "27"):
                return n - i - 2
            if c == "0":
                zero = True
            if c == "5":
                five = True
        return n - zero
