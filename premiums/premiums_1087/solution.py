import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.expand(*test_input)

    def expand(self, s: str) -> List[str]:
            pass