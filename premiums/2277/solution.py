import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.closestNode(*test_input)

    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
                pass