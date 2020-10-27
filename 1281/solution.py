import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.subtractProductAndSum(test_input)

    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        product = 1
        while n > 0:
            digit = n % 10
            sum += digit
            product *= digit
            n = int(n/10)
        return product - sum
