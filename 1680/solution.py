import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.concatenatedBinary(test_input)

    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = ""
        for i in range(n + 1):
            num += "{0:b}".format(i)
        return int(num, 2) % 1000000007
