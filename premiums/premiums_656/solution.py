import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.cheapestJump(*test_input)

    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
            pass