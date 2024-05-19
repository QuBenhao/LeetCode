import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.goodBinaryStrings(*test_input)

    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
                pass