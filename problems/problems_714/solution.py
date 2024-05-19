import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxProfit(*test_input)

    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        dp = [0] * n

        buy = prices[0]

        for i in range(1,n):
            if prices[i] < buy:
                buy = prices[i]
                dp[i] = dp[i-1]
            elif prices[i] - buy > fee:
                dp[i] = dp[i-1] + prices[i] - buy - fee
                buy = prices[i] - fee
            else:
                dp[i] = dp[i-1]

        # print(dp)

        return dp[-1]
