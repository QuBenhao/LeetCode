import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.earliestTime(test_input)

    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min(s + t for s, t in tasks)

