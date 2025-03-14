import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isBalanced(test_input)

    def isBalanced(self, num: str) -> bool:
        ans = 0
        for i, c in enumerate(num):
            if i % 2:
                ans -= int(c)
            else:
                ans += int(c)
        return ans == 0
