import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.concatenatedBinary(test_input)

    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(1, n + 1):
            ans = (ans << i.bit_length() | i) % MOD
        return ans

MOD = 10 ** 9 + 7
