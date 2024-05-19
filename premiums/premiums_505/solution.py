import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.shortestDistance(*test_input)

    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
                pass