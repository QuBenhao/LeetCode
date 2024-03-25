import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.removeInterval(*test_input)

    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
            pass