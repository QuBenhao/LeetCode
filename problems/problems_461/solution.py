import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.hammingDistance(*test_input)

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # return sum(1 for i in range(32) if x >> i & 1 != y >> i & 1)
        # return sum(1 for i in range(len(bin(max(x,y))) - 2) if (x >> i & 1) ^ (y >> i & 1))
        # return bin(x ^ y).count('1')

        a = x ^ y
        ans = 0
        while a > 0:
            a -= a & -a
            ans += 1
        return ans

        # a = x ^ y
        # ans = 0
        # while a > 0:
        #     a &= (a-1)
        #     ans += 1
        # return ans
