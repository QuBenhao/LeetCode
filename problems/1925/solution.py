import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countTriples(test_input)

    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        squares = set([i ** 2 for i in range(1, n + 1)])
        for i in range(1, n + 1):
            for j in range(1, i):
                if i * i + j * j in squares:
                    ans += 2
        return ans
