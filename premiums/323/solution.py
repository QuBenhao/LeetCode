import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countComponents(*test_input)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
            pass