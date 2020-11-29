import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumWealth(test_input)

    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0
        for account in accounts:
            sum = 0
            for num in account:
                sum += num
            if max_wealth < sum:
                max_wealth = sum
        return max_wealth
