import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.calcEquation(*test_input)

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        pass

