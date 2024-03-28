import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.firstDayBeenInAllRooms(test_input)

    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        # f(x + 1) = f(x) + f(x) - f(nextVisit[x]) + 2
        dp, mod = [0] * len(nextVisit), int(1e9 + 7)
        for i in range(1, len(nextVisit)):
            dp[i] = (dp[i - 1] * 2 - dp[nextVisit[i - 1]] + 2) % mod
        return dp[-1]
