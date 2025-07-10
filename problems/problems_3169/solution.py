import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countDays(*test_input)

    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: (x[0], -x[1]))
        ans = 0
        cur = 0
        for start, end in meetings:
            if start <= cur:
                cur = max(cur, end)
                continue
            ans += start - cur - 1
            cur = end
        return ans + days - cur
