import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.mostSimilar(*test_input)

    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
                pass