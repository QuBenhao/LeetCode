import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minArea(*test_input)

    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
                pass