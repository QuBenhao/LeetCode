import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        prices, fee = test_input
        return self.maxProfit(list(prices), fee)

    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
