import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findShortestWay(*test_input)

    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
                pass