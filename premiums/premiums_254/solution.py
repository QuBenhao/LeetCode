import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getFactors(*test_input)

    def getFactors(self, n: int) -> List[List[int]]:
            pass