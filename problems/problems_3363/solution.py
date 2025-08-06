import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxCollectedFruits(test_input)

    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        ans = sum(row[i] for i, row in enumerate(fruits))
        print(ans, fruits)
        dp1 = [0] * n
        dp1[-1] = fruits[0][-1]
        dp2 = [0] * n
        dp2[-1] = fruits[-1][0]
        for i in range(1, n - 1):
            nxt_dp1 = [0] * n
            nxt_dp2 = [0] * n
            for j in range(max(n - i - 1, i + 1), n - 1):
                nxt_dp1[j] = max(dp1[j + 1], dp1[j], dp1[j - 1]) + fruits[i][j]
                nxt_dp2[j] = max(dp2[j + 1], dp2[j], dp2[j - 1]) + fruits[j][i]
            nxt_dp1[n - 1] = max(dp1[n - 1], dp1[n - 2]) + fruits[i][n - 1]
            nxt_dp2[n - 1] = max(dp2[n - 1], dp2[n - 2]) + fruits[n - 1][i]
            dp1 = nxt_dp1
            dp2 = nxt_dp2
        return dp1[-1] + dp2[-1] + ans
