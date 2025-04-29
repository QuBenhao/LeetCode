import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxCount(*test_input)

    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return min(_ops[0]) * min(_ops[1]) if (_ops:= list(zip(*ops))) else m * n
