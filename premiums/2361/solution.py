import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumCosts(*test_input)

    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
                pass