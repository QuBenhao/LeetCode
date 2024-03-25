import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findGameWinner(*test_input)

    def findGameWinner(self, n: int) -> bool:
            pass