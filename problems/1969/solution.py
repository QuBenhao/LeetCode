import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minNonZeroProduct(test_input)

    def minNonZeroProduct(self, p):
        """
        :type p: int
        :rtype: int
        """
        return (m := (2 ** p - 1)) * pow(m - 1, m // 2, (mod := 10 ** 9 + 7)) % mod
