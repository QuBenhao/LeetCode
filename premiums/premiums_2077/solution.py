import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfPaths(*test_input)

    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
            pass