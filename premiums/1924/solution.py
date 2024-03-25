import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.outerTrees(*test_input)

    def outerTrees(self, trees: List[List[int]]) -> List[float]:
            pass