import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxProfit(list(test_input))

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        n = len(prices)
        dp = [0] * n
        curr_min = prices[0]

        for i in range(1, n):
            if prices[i] < curr_min:
                curr_min = prices[i]
                dp[i] = dp[i - 1]
            else:
                dp[i] = max(prices[i] - curr_min, dp[i - 1])
                # curr_min = float("inf")

        return dp[-1]
