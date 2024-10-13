from math import ceil, sqrt

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.twoEggDrop(test_input)

    def twoEggDrop(self, n: int) -> int:
        return ceil(sqrt(n * 8 + 1)) // 2
