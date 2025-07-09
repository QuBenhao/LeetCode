import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxFreeTime(*test_input)

    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)

        def get_dist(idx):
            if idx == 0:
                return startTime[0]
            if idx == n:
                return eventTime - endTime[-1]
            return startTime[idx] - endTime[idx - 1]

        cur = 0
        for i in range(k + 1):
            cur += get_dist(i)
        ans = cur
        for i in range(k + 1, n + 1):
            cur += get_dist(i) - get_dist(i - k - 1)
            ans = max(ans, cur)
        return ans
