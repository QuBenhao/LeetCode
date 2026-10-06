import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumTotalDistance(*test_input)

    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Sort: the greedy property assigns robots to factories in order
        robot.sort()
        factory.sort(key=lambda x: x[0])

        n, m = len(robot), len(factory)

        # Prefix sums: prefix[i] = sum(robot[0:i])
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + robot[i]

        # Precompute cost[l][j] as the total distance for exactly cnt robots from l..n-1 to factory j
        # Use a rolling calculation to avoid extra space

        # dp[i][j] = minimum total distance to assign the first i robots to the first j factories
        INF = 10**18
        dp = [[INF] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for j in range(1, m + 1):
            pos, limit = factory[j - 1]
            dp[0][j] = 0

            for i in range(1, n + 1):
                # Enumerate cnt robots repaired by factory j
                # Robots robot[i-cnt] through robot[i-1] go to pos
                dist = 0
                for cnt in range(min(i, limit) + 1):
                    if cnt > 0:
                        # Update the distance incrementally in O(1)
                        dist += abs(robot[i - cnt] - pos)
                    if dp[i - cnt][j - 1] != INF:
                        dp[i][j] = min(dp[i][j], dp[i - cnt][j - 1] + dist)

        return dp[n][m]

