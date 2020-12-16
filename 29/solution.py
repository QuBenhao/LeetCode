import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        dividend, divisor = test_input
        return self.divide(dividend, divisor)

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        # special case -2^31
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        a, b, res = abs(dividend), abs(divisor), 0
        for x in range(32)[::-1]:
            if (a >> x) - b >= 0:
                res += 1 << x
                a -= b << x
        return res if (dividend > 0) == (divisor > 0) else -res
