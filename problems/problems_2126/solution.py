import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.asteroidsDestroyed(*test_input)

    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        pass

