import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getMaximumConsecutive(list(test_input))

    def getMaximumConsecutive(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        ans = 1
        for coin in sorted(coins):
            if coin <= ans:
                ans += coin
            else:
                return ans
        return ans
