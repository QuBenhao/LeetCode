import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.buildWall(*test_input)

    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
                pass