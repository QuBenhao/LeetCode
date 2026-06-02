from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.earliestFinishTime(*test_input)

    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def solve(first, second):
            min_finish_time = inf
            for s, d in first:
                min_finish_time = min(min_finish_time, s + d)
            return min(max(min_finish_time, s) + d for s, d in second)

        return min(solve(zip(landStartTime, landDuration), zip(waterStartTime, waterDuration)),
                   solve(zip(waterStartTime, waterDuration), zip(landStartTime, landDuration)))
