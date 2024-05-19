import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxIceCream(*test_input)

    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort(reverse=True)
        ans = 0
        while coins and costs:
            if coins < costs[-1]:
                return ans
            coins -= costs.pop()
            ans += 1
        return ans
