import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isConvex(*test_input)

    def isConvex(self, points: List[List[int]]) -> bool:
            pass