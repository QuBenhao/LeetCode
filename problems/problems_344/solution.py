import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        self.reverseString(test_input)
        return test_input

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
