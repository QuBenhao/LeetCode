import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.differenceOfSums(*test_input)

    def differenceOfSums(self, n: int, m: int) -> int:
        return (1 + n) * n // 2 - m * (d := n // m) * (1 + d)
