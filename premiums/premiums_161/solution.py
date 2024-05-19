import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isOneEditDistance(*test_input)

    def isOneEditDistance(self, s: str, t: str) -> bool:
            pass