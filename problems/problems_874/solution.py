import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.robotSim(*test_input)

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        pass

