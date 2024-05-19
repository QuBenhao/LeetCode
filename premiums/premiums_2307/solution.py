import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.checkContradictions(*test_input)

    def checkContradictions(self, equations: List[List[str]], values: List[float]) -> bool:
            pass