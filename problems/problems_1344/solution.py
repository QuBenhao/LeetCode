import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.angleClock(*test_input)

    def angleClock(self, hour: int, minutes: int) -> float:
        hour %= 12
        return min(a := abs((hour * 60 + minutes) / 2 - minutes * 6), 360 - a)
