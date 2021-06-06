import solution
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        strs, m, n = test_input
        return self.findMaxForm(list(strs), m, n)

    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

        # dp = [[0] * (n+1) for _ in range(m+1)]
        # for s in strs:
        #     ones = s.count('1')
        #     zeros = len(s) - ones
        #     if ones > n or zeros > m:
        #         continue
        #     for i in range(m-zeros,-1,-1):
        #         for j in range(n-ones,-1,-1):
        #             dp[i+zeros][j+ones] = max(dp[i+zeros][j+ones], dp[i][j] + 1)
        # return dp[m][n]

        @lru_cache(None)
        def dfs(idx, x, y):
            if x < 0 or y < 0:
                return float("-inf")
            if idx == l:
                return 0
            ones = strs[idx].count('1')
            zeros = len(strs[idx]) - ones
            # 选当前idx和不选当前idx的最大值
            return max(dfs(idx + 1, x - zeros, y - ones) + 1, dfs(idx + 1, x, y))

        l = len(strs)
        return dfs(0, m, n)
