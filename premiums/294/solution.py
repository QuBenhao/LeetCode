import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canWin(*test_input)

    def canWin(self, currentState: str) -> bool:
            pass