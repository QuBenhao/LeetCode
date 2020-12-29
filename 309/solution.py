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
        # can buy, can sell, need rest
        s0, s1, s2 = 0, -prices[0], float("-inf")
        # s0 = max(s0,s2)
        # s1 = max(s1,s0-prices[i])
        # s2 = max(s2,s1+prices[i])
        # res = max(s0,s2)

        for i in range(1, n):
            temp = s2
            s2 = max(s2, s1 + prices[i])
            s1 = max(s1, s0 - prices[i])
            s0 = max(s0, temp)

        return max(s0, s2)
