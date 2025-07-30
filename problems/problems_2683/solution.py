import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.doesValidArrayExist(test_input)

    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return sum(derived) % 2 == 0
