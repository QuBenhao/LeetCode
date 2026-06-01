import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.earliestFinishTime(*test_input)

    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        pass

