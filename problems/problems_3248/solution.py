import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.finalPositionOfSnake(*test_input)

    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        i, j = 0, 0
        for command in commands:
            match command:
                case "UP":
                    i -= 1
                case "DOWN":
                    i += 1
                case "LEFT":
                    j -= 1
                case _:
                    j += 1
        return n * i + j
