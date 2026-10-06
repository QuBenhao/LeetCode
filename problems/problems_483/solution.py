import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.smallestGoodBase(test_input)

    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        num = int(n)
        # n = x^(m-1) + x^(m-2) + ... + x + 1
        for m in range(num.bit_length(),2,-1):
            # Binomial expansion: x^(m-1) < n < (x+1)^(m-1)
            x = int(pow(num,1/(m-1)))
            # Geometric series sum: n = (x^m - 1)/(x-1)
            if num == (pow(x,m) - 1)//(x-1):
                return str(x)
        return str(num-1)
