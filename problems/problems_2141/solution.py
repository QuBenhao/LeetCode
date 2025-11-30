import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxRunTime(*test_input)

    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort(reverse=True)
        s = sum(batteries)
        for b in batteries:
            if b <= s // n:
                return s // n
            s -= b
            n -= 1
        return -1
