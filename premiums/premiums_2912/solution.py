import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfWays(*test_input)

    def numberOfWays(self, n: int, m: int, k: int, source: List[int], dest: List[int]) -> int:
                    pass