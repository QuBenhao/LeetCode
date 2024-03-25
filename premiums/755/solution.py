import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.pourWater(*test_input)

    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
                pass