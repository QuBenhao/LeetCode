import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        self.merge(*test_input)
        return *test_input

    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        pass

