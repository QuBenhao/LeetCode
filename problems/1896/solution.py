import solution
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minOperationsToFlip(str(test_input))

    def minOperationsToFlip(self, expression):
        """
        :type expression: str
        :rtype: int
        """
