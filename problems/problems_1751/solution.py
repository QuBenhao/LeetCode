import solution
import bisect


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxValue(*test_input)

    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """
        events.sort(key=lambda x: x[1])
        n = len(events)
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(n):
            p = bisect.bisect_left(events, events[i][0], hi=i, key=lambda x: x[1])
            for j in range(1, k + 1):
                dp[i + 1][j] = max(dp[i][j], dp[p][j - 1] + events[i][2])
        return dp[n][k]
