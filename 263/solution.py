import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isUgly(test_input)

    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        for factor in 2, 3, 5:
            while n % factor == 0:
                n /= factor
        return n == 1
