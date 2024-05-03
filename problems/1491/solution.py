import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.average(test_input)

    def average(self, salary: List[int]) -> float:
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)
