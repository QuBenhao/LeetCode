import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.furthestDistanceFromOrigin(test_input)

    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return abs((l := moves.count('L')) - (r :=  moves.count('R'))) + len(moves) - l - r
