import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findClosest(*test_input)

    def findClosest(self, x: int, y: int, z: int) -> int:
        d1, d2 = abs(x - z), abs(y - z)
        return 1 if d1 < d2 else (2 if d2 < d1 else 0)
