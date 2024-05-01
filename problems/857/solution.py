import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.mincostToHireWorkers(*test_input)

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
                pass