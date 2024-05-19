import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findBlackPixel(*test_input)

    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
            pass