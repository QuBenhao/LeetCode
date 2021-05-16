import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        n, k = test_input
        return self.sumBase(n, k)

    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if not n:
            return 0
        return self.sumBase(n // k, k) + n % k
