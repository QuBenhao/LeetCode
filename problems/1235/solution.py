import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.jobScheduling(*test_input)

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
                pass