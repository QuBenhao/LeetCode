import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.judgeCircle(test_input)

    def judgeCircle(self, moves: str) -> bool:
        horizontal, vertical = 0, 0
        for c in moves:
            match c:
                case 'U':
                    vertical += 1
                case 'D':
                    vertical -= 1
                case 'L':
                    horizontal -= 1
                case _:
                    horizontal += 1
        return horizontal == 0 and vertical == 0
