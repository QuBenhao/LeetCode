import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.verifyPreorder(*test_input)

    def verifyPreorder(self, preorder: List[int]) -> bool:
            pass