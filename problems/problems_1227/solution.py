import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.nthPersonGetsNthSeat(test_input)

    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1 if n == 1 else 0.5
