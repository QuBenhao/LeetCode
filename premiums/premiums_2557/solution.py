import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxCount(*test_input)

    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
                pass