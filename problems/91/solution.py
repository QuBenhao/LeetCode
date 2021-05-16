import solution
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numDecodings(str(test_input))

    @lru_cache(None)
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s and int(s[0]) == 0:
            return 0
        if len(s) <= 1:
            return 1
        if int(s[:2]) <= 26:
            return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
        return self.numDecodings(s[1:])

        # n = len(s)
        # s = '0' + s
        # f = [0] * 3
        # f[0] = 1
        # for i in range(1,n+1):
        #     f[i % 3] = 0
        #     a,b = int(s[i]),int(s[i-1:i+1])
        #     if 1 <= a <= 9:
        #         f[i % 3] = f[(i - 1) % 3]
        #     if 10 <= b <= 26:
        #         f[i % 3] += f[(i - 2) % 3]
        # return f[n % 3]
