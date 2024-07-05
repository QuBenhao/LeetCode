import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isUnique(test_input)


    def isUnique(self, astr: str) -> bool:
        return len(set(astr)) == len(astr)

