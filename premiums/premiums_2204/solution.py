import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.distanceToCycle(*test_input)

    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
            pass