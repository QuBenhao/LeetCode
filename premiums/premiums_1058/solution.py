import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimizeError(*test_input)

    def minimizeError(self, prices: List[str], target: int) -> str:
            pass