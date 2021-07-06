import solution
from functools import lru_cache
from math import log


class Solution(solution.Solution):
    def solve(self, test_input=None):
        k, n = test_input
        return self.superEggDrop(k, n)

    # @lru_cache(None)
    # def superEggDrop(self, k, n):
    #     """
    #     :type k: int
    #     :type n: int
    #     :rtype: int
    #     """
    #     if k == 1 or n <= 2:
    #         return n
    #     # 如果k比n大，我们可以每个楼层用一个鸡蛋，最快的方法就是二分
    #     if k >= n:
    #         return int(log(n, 2)) + 1
    #     # 假设初始扔的第一个楼层为x,如果鸡蛋碎了，那么问题变为用k-1个鸡蛋解决x-1个楼层; 如果没碎，问题变为k个鸡蛋解决n-x个楼层
    #     # 如果x越大，左边越大，右边越小; x越小左边越小，右边越大
    #     ans = n
    #     left, right = 1, n
    #     while left < right:
    #         mid = (left + right) // 2
    #         l = self.superEggDrop(k-1,mid-1)
    #         r = self.superEggDrop(k, n-mid)
    #         ans = min(ans, max(l, r) + 1)
    #         if l >= r:
    #             right = mid
    #         else:
    #             left = mid + 1
    #     return ans

    def superEggDrop(self, k: int, n: int) -> int:
        # 反过来想，给我们k个鸡蛋，m次尝试机会，我们最多能测出多少层？
        # 我们扔一个鸡蛋，鸡蛋可能碎了，也可能没碎。
        # 如果鸡蛋没碎，我们就能解决dp[k][m-1]层；如果鸡蛋碎了，我们就能解决dp[k-1][m-1]层;再加上第一个扔的层。
        # 有: dp[k][m] = dp[k][m-1] + dp[k-1][m-1] + 1.
        # 问题变为求最小的m使得dp[k][m] >= n
        for i in range(1, n + 1):
            if self.maximumFloors(k, i) >= n:
                return i
        return n

    @lru_cache(None)
    def maximumFloors(self, k, m):
        if k == 0:
            return 0
        if m == 1:
            return 1
        return self.maximumFloors(k, m - 1) + self.maximumFloors(k - 1, m - 1) + 1
