from math import floor, sqrt

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minNumberOfSeconds(*test_input)

    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def check(x: int) -> bool:
            s = 0
            for wt in workerTimes:
                if x < wt:
                    continue
                # (t + 1) * t * wt / 2 <= x
                # (t + 1) * t <= 2 * x / wt
                # t * t < (t + 1) * t <= 2 * x / wt
                t = floor(sqrt(2 * x / wt))
                while (t + 1) * t * wt // 2 <= x:
                    t += 1
                s += t - 1
                if s >= mountainHeight:
                    return True
            return False

        left, right = 1, (mountainHeight + 1) * mountainHeight // 2 * max(workerTimes)
        while left < right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
