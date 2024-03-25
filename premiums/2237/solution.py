import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.meetRequirement(*test_input)

    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
                pass