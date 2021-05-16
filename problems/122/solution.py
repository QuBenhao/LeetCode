import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxProfit(list(test_input))

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)

        profit = 0

        for i in range(1,n):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit

        # n = len(prices)
        # dp = [0] * n
        #
        # buy = prices[0]
        #
        # for i in range(1,n):
        #     if prices[i] < buy:
        #         buy = prices[i]
        #         dp[i] = dp[i-1]
        #     else:
        #         dp[i] = dp[i-1] + prices[i] - buy
        #         buy = prices[i]
        #
        # print(dp)
        #
        # return dp[-1]

