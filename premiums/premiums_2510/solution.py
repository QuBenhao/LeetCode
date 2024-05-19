import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isThereAPath(*test_input)

    def isThereAPath(self, grid: List[List[int]]) -> bool:
            pass