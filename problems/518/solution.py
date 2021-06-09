import solution
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        amount, coins = test_input
        return self.change(amount, list(coins))

    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        # @lru_cache(None)
        # def dfs(total, idx):
        #     if total > amount or idx == len(coins):
        #         return 0
        #     elif total == amount:
        #         return 1
        #     if total + coins[idx] > amount:
        #         return 0
        #     return dfs(total + coins[idx], idx) + dfs(total, idx + 1)
        #
        # coins.sort()
        # return dfs(0, 0)

        dp = [1] + [0] * amount
        for c in coins:
            for i in range(c, amount+1):
                dp[i] += dp[i-c]
        return dp[amount]
