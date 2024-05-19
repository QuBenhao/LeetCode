import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findPattern(*test_input)

    def findPattern(self, board: List[List[int]], pattern: List[str]) -> List[int]:
            pass