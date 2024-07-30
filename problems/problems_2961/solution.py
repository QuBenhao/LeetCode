import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getGoodIndices(*test_input)

    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        return [i for i, (a, b, c, m) in enumerate(variables) if pow(pow(a, b, 10), c, m) == target]
