import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.losingPlayer(*test_input)

    def losingPlayer(self, x: int, y: int) -> str:
        m = min(x * 4, y) // 4
        return "Alice" if m % 2 == 1 else "Bob"
