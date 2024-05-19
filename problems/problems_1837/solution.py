import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sumBase(*test_input)

    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if not n:
            return 0
        return self.sumBase(n // k, k) + n % k
