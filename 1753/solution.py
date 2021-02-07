import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        a, b, c = test_input
        return self.maximumScore(a, b, c)

    def maximumScore(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        return min((a + b + c) // 2, a + b + c - max(a, b, c))

        # s = a + b + c
        # a, c = min(a,b,c), max(a,b,c)
        # b = s - a - c
        # ans = 0
        # while b > 0:
        #     if b == a:
        #         curr = 1
        #         a -= 1
        #         c -= curr
        #     else:
        #         curr = b - a
        #         b -= curr
        #         c -= curr
        #     ans += curr
        #     s = a + b + c
        #     a, c = min(a,b,c), max(a,b,c)
        #     b = s - a - c
        # return ans
