import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.garbageCollection(*test_input)

    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
            pass