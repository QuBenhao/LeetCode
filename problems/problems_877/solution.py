import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.stoneGame(list(test_input))

    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        # 先手可以永远拿奇数位或者永远拿偶数位,两个里面更大的那个是必胜的
        # return True

        # # dp[i][j]的最大值由(piles[i]-dp[i+1][j],piles[j]-dp[i][j-1])决定
        # # 要先求长度短的
        # n = len(piles)
        # dp = [[piles[i]] * n for i in range(n)]
        # # 长度为1到n
        # for length in range(2, n + 1):
        #     # 枚举左端点
        #     for i in range(n - length + 1):
        #         # 对应的右端点
        #         j = i + length - 1
        #         dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        # # print(dp)
        # return dp[0][n - 1] > 0

        # 优化为一维
        n = len(piles)
        dp = list(piles)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])
        print(dp)
        return dp[n - 1] > 0
