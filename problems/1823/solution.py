import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findTheWinner(*test_input)

    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 1:
            return n
        return (self.findTheWinner(n - 1, k) + k - 1) % n + 1
