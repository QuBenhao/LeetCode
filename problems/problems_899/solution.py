import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.orderlyQueue(*test_input)

    def orderlyQueue(self, s: str, k: int) -> str:
        return min(s[i:] + s[:i] for i in range(len(s))) if k == 1 else ''.join(sorted(s))
