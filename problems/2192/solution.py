import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getAncestors(*test_input)

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
            pass