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
        证明：设a = m * c + x, b = n * c + y
            a * b = m * n * c * c + x * n * c + y * m * c + x * y
            故 a * b % c = x * y % c
        """
        # 由上面结论可以得到如下两个性质
        # 4的幂满足模3余1（每个4都是模3余1，乘起来也模3余1）
        # 2的奇数次幂满足一个4的幂乘上一个2，相当于一个模3余1的数和模3余2的数相乘,所以模3余2
        # 故 2的奇数次幂和偶数次幂模3是不同的
        return n & (n-1) == 0 and n % 3 == 1 if n > 0 else False
