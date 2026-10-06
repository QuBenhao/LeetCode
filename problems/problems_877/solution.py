import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.stoneGame(list(test_input))

    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        # The first player can always take odd positions or always take even positions; choosing the larger sum guarantees a win
        # return True

        # # The maximum dp[i][j] is determined by (piles[i]-dp[i+1][j],piles[j]-dp[i][j-1])
        # # Compute shorter intervals first
        # n = len(piles)
        # dp = [[piles[i]] * n for i in range(n)]
        # # Lengths from 1 to n
        # for length in range(2, n + 1):
        #     # Enumerate left endpoints
        #     for i in range(n - length + 1):
        #         # Corresponding right endpoint
        #         j = i + length - 1
        #         dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        # # print(dp)
        # return dp[0][n - 1] > 0

        # Optimize to one dimension
        n = len(piles)
        dp = list(piles)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])
        print(dp)
        return dp[n - 1] > 0
