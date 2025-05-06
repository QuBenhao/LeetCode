import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.knightDialer(test_input)

    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        mod = int(1e9) + 7
        """
        1: 6, 8
        2: 7, 9
        3: 4, 8
        4: 3, 9, 0
        5: -
        6: 1, 7, 0
        7: 2, 6
        8: 1, 3
        9: 2, 4
        0: 4, 6
        """
        dp = [[1] * 10 for _ in range(2)]
        for i in range(1, n):
            dp[i%2][0] = (dp[(i-1)%2][4] + dp[(i-1)%2][6]) % mod
            dp[i%2][1] = (dp[(i-1)%2][6] + dp[(i-1)%2][8]) % mod
            dp[i%2][2] = (dp[(i-1)%2][7] + dp[(i-1)%2][9]) % mod
            dp[i%2][3] = (dp[(i-1)%2][4] + dp[(i-1)%2][8]) % mod
            dp[i%2][4] = (dp[(i-1)%2][3] + dp[(i-1)%2][9] + dp[(i-1)%2][0]) % mod
            dp[i%2][5] = 0
            dp[i%2][6] = (dp[(i-1)%2][1] + dp[(i-1)%2][7] + dp[(i-1)%2][0]) % mod
            dp[i%2][7] = (dp[(i-1)%2][2] + dp[(i-1)%2][6]) % mod
            dp[i%2][8] = (dp[(i-1)%2][1] + dp[(i-1)%2][3]) % mod
            dp[i%2][9] = (dp[(i-1)%2][2] + dp[(i-1)%2][4]) % mod
        return sum(dp[(n-1)%2]) % mod
