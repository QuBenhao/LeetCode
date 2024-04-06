import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxProfit(list(test_input))

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hold1, sell1, hold2, sell2 = -prices[0], 0, -prices[0], 0
        for p in prices:
            hold1 = max(hold1, -p)
            sell1 = max(sell1, hold1 + p)
            hold2 = max(hold2, sell1 - p)
            sell2 = max(sell2, hold2 + p)
        return sell2
