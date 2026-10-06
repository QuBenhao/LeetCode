import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isPowerOfFour(test_input)

    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # a % c = x, b % c = y --> ab % c = xy % c
        """
        Proof: Let a = m * c + x, b = n * c + y.
            a * b = m * n * c * c + x * n * c + y * m * c + x * y
            Therefore, a * b % c = x * y % c.
        """
        # The conclusion above gives two properties
        # Powers of 4 have remainder 1 modulo 3 (each factor 4 has remainder 1, so their product does too)
        # An odd power of 2 is a power of 4 times 2, so its remainder modulo 3 is 1 times 2, or 2
        # Thus, odd and even powers of 2 have different remainders modulo 3
        return n & (n-1) == 0 and n % 3 == 1 if n > 0 else False
