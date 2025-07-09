import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxFreeTime(*test_input)

    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        distances = [startTime[0]] + [s - e for s, e in zip(startTime[1:], endTime[:-1])] + [eventTime - endTime[-1]]
        a, b, c = -1, -1, -1
        for i in range(n + 1):
            d = distances[i]
            if a == -1 or d >= distances[a]:
                a, b, c = i, a, b
            elif b == -1 or d >= distances[b]:
                b, c = i, b
            elif c == -1 or d > distances[c]:
                c = i

        def get_max(idx: int) -> int:
            if a != idx and a != idx + 1:
                return distances[a]
            if b != idx and b != idx + 1:
                return distances[b]
            return distances[c]

        ans = 0
        for i, (s, e) in enumerate(zip(startTime, endTime)):
            if get_max(i) >= (cur := e - s):
                ans = max(ans, distances[i] + distances[i + 1] + cur)
            else:
                ans = max(ans, distances[i] + distances[i + 1])
        return ans
