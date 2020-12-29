import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxProfit(list(test_input))

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        times = 2
        n = len(prices)
        dp = [[0 for i in range(n)] for i in range(times)]

        curr_min = buy = prices[0]
        last = -1
        for i in range(1, n):
            if prices[i] <= buy:
                buy = prices[i]
                dp[0][i] = dp[0][i - 1]
                dp[1][i] = dp[1][i - 1]
            else:
                dp[1][i] = max(prices[i] - curr_min, dp[1][i - 1])
                if last > 0:
                    dp[0][i] = max(dp[1][i-1] + prices[i] - buy,dp[0][last]+prices[i]-prices[last])
                buy = prices[i]
                last = i
            curr_min = min(curr_min, buy)

        # print(dp)

        return max(max(dp[0]), dp[1][-1])
