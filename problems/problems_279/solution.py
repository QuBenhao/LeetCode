import solution
from functools import lru_cache
from math import inf,sqrt


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numSquares(test_input)

    def numSquares(self, n: int) -> int:
        # dp = [0] + [inf] * n
        # rg = int(sqrt(n))
        # for i in range(1, rg + 1):
        #     curr = i * i
        #     for j in range(curr,n+1):
        #         dp[j] = min(dp[j],dp[j-curr]+1)
        # return dp[n]

        # 次数筛的贪心
        ps = set([i * i for i in range(1, int(n ** 0.5) + 1)])

        def divisible(n, count):
            if count == 1: return n in ps
            for p in ps:
                if divisible(n - p, count - 1):
                    return True
            return False

        for count in range(1, n + 1):
            if divisible(n, count):
                return count

    # @lru_cache(None)
    # def numSquares(self, n: int) -> int:
    #     if n == int(sqrt(n)) ** 2:
    #         return 1
    #     # 次数筛
    #     for i in range(2,n+1):
    #         # 次数i对应的平方数至少有一个大于等于平均数n//i
    #         for j in range(int(sqrt(n//i)), int(sqrt(n))+1):
    #             if self.numSquares(n-j*j) + 1 == i:
    #                 return i
    #     return n
