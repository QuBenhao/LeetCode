import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        n, x = test_input
        return self.maxValue(str(n), x)

    def maxValue(self, n, x):
        """
        :type n: str
        :type x: int
        :rtype: str
        """
        if n[0] == '-':
            for i, c in enumerate(n[1:], 1):
                if int(c) > x:
                    return n[:i] + str(x) + n[i:]
            return n + str(x)
        else:
            for i, c in enumerate(n):
                if int(c) < x:
                    return n[:i] + str(x) + n[i:]
            return n + str(x)
