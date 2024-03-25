import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isPreorder(*test_input)

    def isPreorder(self, nodes: List[List[int]]) -> bool:
            pass