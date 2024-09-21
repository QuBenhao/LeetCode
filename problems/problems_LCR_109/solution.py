import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.openLock(*test_input)

    def openLock(self, deadends: List[str], target: str) -> int:
        pass

