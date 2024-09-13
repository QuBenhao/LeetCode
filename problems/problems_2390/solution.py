import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.removeStars(test_input)

    def removeStars(self, s: str) -> str:
        ans = []
        for c in s:
            if c == "*" and ans:
                ans.pop()
            elif c != "*":
                ans.append(c)
        return "".join(ans)
