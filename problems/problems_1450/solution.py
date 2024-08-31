import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.busyStudent(*test_input)

    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(s <= queryTime <= e for s, e in zip(startTime, endTime))
