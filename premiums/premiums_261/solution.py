import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.validTree(*test_input)

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
            pass