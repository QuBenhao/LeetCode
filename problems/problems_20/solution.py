import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isValid(test_input)

    def isValid(self, s: str) -> bool:
        stack = []
        left, right = "{[(", "}])"
        for c in s:
            if c in left:
                stack.append(c)
            elif not stack or left.index(stack.pop()) != right.index(c):
                return False
        return not stack
