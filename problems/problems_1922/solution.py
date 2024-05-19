import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countGoodNumbers(test_input)

    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 偶数位 0, 2, 4, 6, 8； 奇数位 2, 3, 5, 7
        mod = 10 ** 9 + 7
        return pow(20, n//2, mod) if n % 2 == 0 else pow(20, n//2, mod) * 5 % mod
