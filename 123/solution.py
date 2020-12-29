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
