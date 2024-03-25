import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.earliestAcq(*test_input)

    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
            pass