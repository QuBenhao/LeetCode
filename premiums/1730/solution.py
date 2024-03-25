import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getFood(*test_input)

    def getFood(self, grid: List[List[str]]) -> int:
            pass