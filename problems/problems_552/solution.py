import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.checkRecord(test_input)

    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        # mod = 10 ** 9 + 7
        # alast, alastL, alastLL, last, lastL, lastLL = 1, 0, 0, 1, 1, 0
        # for i in range(2, n + 2):
        #     alast, alastL, alastLL, last, lastL, lastLL = (alastLL + alastL + alast + last + lastL + lastLL) % mod,alast,alastL,(last + lastL + lastLL) % mod,last,lastL
        # return alast

        import numpy as np

        mod = 10 ** 9 + 7
        cell = np.diag([1] * 6)
        mul = np.array(
            [[1, 1, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 0, 0, 1, 1, 1], [1, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 1, 0]])
        n -= 1
        while n:
            if n & 1:
                cell = np.mod(np.dot(cell, mul), mod)
            mul = np.mod(np.dot(mul, mul), mod)
            n >>= 1
        ans = np.mod(np.dot(cell, np.array([1, 1, 0, 0, 0, 0])), mod)
        return int((sum(ans) + ans[0]) % mod)
