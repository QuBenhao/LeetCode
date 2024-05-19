import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumDistance(*test_input)

    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
                pass