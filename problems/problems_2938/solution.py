import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumSteps(test_input)

    def minimumSteps(self, s: str) -> int:
        ans, b = 0, 0
        for c in s:
            if c == "0":
                ans += b
            else:
                b += 1
        return ans
