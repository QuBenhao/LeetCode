import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.finalValueAfterOperations(test_input)

    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(1 if operation[1] == "+" else -1 for operation in operations)
