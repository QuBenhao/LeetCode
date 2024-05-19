import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.generatePossibleNextMoves(*test_input)

    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
            pass