import solution
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numWays(*test_input)

    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        # # Memoized DFS
        # @lru_cache(None)
        # def dfs(cur, s):
        #     if cur == -1 or cur == arrLen or cur > s:
        #         return 0
        #     if cur <= 1 and s == 1:
        #         return 1
        #     s -= 1
        #     return dfs(cur, s) + dfs(cur - 1, s) + dfs(cur + 1, s)
        #
        # return dfs(0, steps) % (10 ** 9 + 7)

        # # One-dimensional dynamic programming with bottom-up rolling updates
        # if arrLen == 1 or steps == 1:
        #     return 1
        # dp = [0] * (min(steps // 2 + 1, arrLen) + 2)
        # n = len(dp)
        # dp[1] = dp[2] = 1
        # for i in range(1, steps):
        #     nxt_dp = [0] * n
        #     for j in range(1, min(n - 1, i + 3, steps - i + 1)):
        #         nxt_dp[j] = dp[j-1] + dp[j] + dp[j+1]
        #     dp = nxt_dp
        # return dp[1] % (10 ** 9 + 7)

        # One-dimensional dynamic programming with bottom-up rolling updates and the mathematical optimization
        if arrLen == 1 or steps == 1:
            return 1
        dp = [0] * (min(steps // 2 + 1, arrLen) + 2)
        n = len(dp)
        dp[1] = dp[2] = 1
        # Symmetry: dp at half of steps is enough, because working back toward position 0 is the same as working forward from position 0
        for i in range(1, steps // 2):
            nxt_dp = [0] * n
            for j in range(1, min(n - 1, i + 3)):
                nxt_dp[j] = dp[j-1] + dp[j] + dp[j+1]
            dp = nxt_dp
        # An even-numbered row is the sum of squares of its middle row
        if steps % 2 == 0:
            return sum(x**2 for x in dp) % (10 ** 9 + 7)
        # An odd-numbered row is the dot product of its two middle rows
        return sum(dp[i] * (dp[i-1] + dp[i] + dp[i+1]) for i in range(1,len(dp)-1)) % (10 ** 9 + 7)
