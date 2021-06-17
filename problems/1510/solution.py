import solution
from functools import lru_cache
import math


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.winnerSquareGame(test_input)

    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        @lru_cache(None)
        def dfs(curr):
            if not curr:
                return False
            for i in range(int(math.sqrt(curr)),0,-1):
                if not dfs(curr-i*i):
                    return True
            return False

        return dfs(n)

        # dp = {0}
        # for i in range(1, n+1):
        #     if all(i-j*j not in dp for j in range(int(math.sqrt(i)), 0, -1)):
        #         dp.add(i)
        # return n not in dp
