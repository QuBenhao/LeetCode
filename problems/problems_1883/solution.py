import solution
from math import ceil


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minSkips(*test_input)

    def minSkips(self, dist, speed, hoursBefore):
        """
        :type dist: List[int]
        :type speed: int
        :type hoursBefore: int
        :rtype: int
        """
        # Avoid floating-point error: ceil(8.0+1.0/3+1.0/3+1.0/3) is 10 instead of 9
        eps = 1e-9
        n = len(dist)
        # Any value beyond the deadline suffices; float("inf") would require special handling in later additions
        dp = [[10 ** 7 + 1] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i, d in enumerate(dist, 1):
            # Skip no rests
            dp[i][0] = ceil(dp[i - 1][0] + d / speed - eps)
            # At i, at most i rests can have been skipped
            for j in range(1, i + 1):
                # For j skips, either skip now after j-1 earlier skips or rest now after j earlier skips
                dp[i][j] = min(dp[i - 1][j - 1] + d / speed, ceil(dp[i - 1][j] + d / speed - eps))

        for j, t in enumerate(dp[-1]):
            # Scan left to right for the minimum skips that allow an on-time arrival
            if t <= hoursBefore:
                return j
        return -1
