import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countDaysTogether(*test_input)

    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        l, r = max(arriveAlice, arriveBob), min(leaveAlice, leaveBob)
        if l > r:
            return 0

        def cal_days(s):
            idx = int(s[:2])
            d = 0
            for i in range(idx - 1):
                d += days[i]
            return d + int(s[3:])

        return cal_days(r) - cal_days(l) + 1
