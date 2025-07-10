import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.flipLights(*test_input)

    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0:
            return 1
        if n == 1:
            return 2
        if n == 2:
            return 3 if presses == 1 else 4
        return 4 if presses == 1 else (7 if presses == 2 else 8)
