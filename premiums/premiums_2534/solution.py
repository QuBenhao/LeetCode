import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.timeTaken(*test_input)

    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
            pass