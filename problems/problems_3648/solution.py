import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minSensors(*test_input)

    def minSensors(self, n: int, m: int, k: int) -> int:
        k = 2 * k + 1
        return ((n - 1) // k + 1) * ((m - 1) // k + 1)
