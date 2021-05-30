import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isPowerOfTwo(test_input)

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n & -n == n if n > 0 else False
        # return n & (n-1) == 0 if n > 0 else False
