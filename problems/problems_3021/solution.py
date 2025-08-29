import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.flowerGame(*test_input)

    def flowerGame(self, n: int, m: int) -> int:
        return (n // 2) * ((m + 1) // 2) + ((n + 1) // 2) * (m // 2)
