import solution
import math


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isThree(test_input)

    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def isPrime(x):
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    return False
            return True if x > 1 else False

        p = int(math.sqrt(n))
        return p * p == n and isPrime(p)
