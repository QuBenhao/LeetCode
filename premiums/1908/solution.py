import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.nimGame(*test_input)

    def nimGame(self, piles: List[int]) -> bool:
            pass