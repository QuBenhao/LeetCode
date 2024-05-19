import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.hasPath(*test_input)

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
                pass