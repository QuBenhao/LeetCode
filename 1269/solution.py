import solution
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numWays(test_input[0], test_input[1])

    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        # # 记忆化dfs
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

        # 一维数组动态规划，自底向上滚动更新
        if arrLen == 1 or steps == 1:
            return 1
        dp = [0] * (min(steps // 2 + 1, arrLen) + 2)
        n = len(dp)
        dp[1] = dp[2] = 1
        for i in range(1, steps):
            nxt_dp = [0] * n
            for j in range(1, min(n - 1, i + 3, steps - i + 1)):
                nxt_dp[j] = dp[j-1] + dp[j] + dp[j+1]
            dp = nxt_dp
        return dp[1] % (10 ** 9 + 7)
