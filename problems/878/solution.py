import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        n, a, b = test_input
        return self.nthMagicalNumber(n, a, b)

    def nthMagicalNumber(self, n, a, b):
        """
        :type n: int
        :type a: int
        :type b: int
        :rtype: int
        """
        mod = 10 ** 9 + 7

        """
        4 points to figure out:

        1.Get gcd (greatest common divisor) and lcm (least common multiple) of (A, B).
        (a, b) = (A, B) while b > 0: (a, b) = (b, a % b)
        then, gcd = a and lcm = A * B / a
        
        2.How many magic numbers <= x ?
        By inclusion exclusion principle, we have:
        x / A + x / B - x / lcm
        
        3.Set our binary search range
        Lower bound is min(A, B), I just set left = 2.
        Upper bound is N * min(A, B), I just set right = 10 ^ 14.
        
        4.binary search, find the smallest x that x / A + x / B - x / lcm = N
        """

        x, y = a, b
        while y:
            x, y = y, x % y
        l, r, lcm = 2, 10 ** 14, a * b // x
        while l < r:
            m = (l + r) // 2
            if m // a + m // b - m // lcm < n:
                l = m + 1
            else:
                r = m
        return l % mod

        # def gcd(a, b):
        #     if b == 0:
        #         return a
        #     else:
        #         return gcd(b, a % b)

        # if a > b:
        #     temp = a
        #     a = b
        #     b = temp
        # if b % a == 0:
        #     return n * a % mod
        # gcd = gcd(a,b)
        # lcm = a*b//gcd
        # nums = []
        # for i in range(1,lcm//a+1):
        #     nums.append(i*a)
        # for i in range(1,lcm//b):
        #     nums.append(i*b)
        # nums.sort()
        # times = n//len(nums)
        # index = n%len(nums) -1
        # # print(nums,times,index)
        # if index == -1:
        #     return times*lcm % mod
        # return (times*lcm + nums[index])%mod
