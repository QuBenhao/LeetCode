import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.totalMoney(test_input)

    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        d, r = divmod(n, 7)
        # 1 + 2 + ... + 7 = 28
        return d * 28 + 7 * d * (d - 1) // 2 + (d + 1 + d + r) * r // 2
