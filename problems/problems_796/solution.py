import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.rotateString(*test_input)

    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s
