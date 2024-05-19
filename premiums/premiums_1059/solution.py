import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.leadsToDestination(*test_input)

    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
                pass