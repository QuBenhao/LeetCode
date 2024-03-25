import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumHealth(*test_input)

    def minimumHealth(self, damage: List[int], armor: int) -> int:
            pass