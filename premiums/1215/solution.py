import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countSteppingNumbers(*test_input)

    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
            pass