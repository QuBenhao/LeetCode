from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxTwoEvents(test_input)

    def maxTwoEvents(self, events: List[List[int]]) -> int:
        times = set()
        for a, b, _ in events:
            times.add(a)
            times.add(b)
        tm = dict()
        st = list(sorted(times))
        for i, t in enumerate(st):
            tm[t] = i
        # dp[i][0]表示到时间i的选过一次的最大值, dp[i][1]表示到时间i的选过两次的最大值
        dp = [[0, 0] for _ in range(len(st) + 1)]
        events_map = defaultdict(list)
        for i, (_, b, _) in enumerate(events):
            events_map[tm[b]].append(i)
        for i in range(len(st)):
            dp[i+1][0] = dp[i][0]
            dp[i+1][1] = dp[i][1]
            for j in events_map[i]:
                dp[i+1][0] = max(dp[i + 1][0], events[j][2])
                dp[i+1][1] = max(dp[i+1][1], dp[tm[events[j][0]]][0] + events[j][2])
        return dp[-1][-1]
