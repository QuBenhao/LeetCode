import solution
from functools import lru_cache
from math import log


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.superEggDrop(*test_input)

    # @lru_cache(None)
    # def superEggDrop(self, k, n):
    #     """
    #     :type k: int
    #     :type n: int
    #     :rtype: int
    #     """
    #     if k == 1 or n <= 2:
    #         return n
    #     # If k exceeds n, we can use one egg per floor; binary search is the fastest approach
    #     if k >= n:
    #         return int(log(n, 2)) + 1
    #     # Suppose the first drop is from floor x: if the egg breaks, solve x-1 floors with k-1 eggs; otherwise, solve n-x floors with k eggs
    #     # As x increases, the left side increases and the right decreases; as x decreases, the left decreases and the right increases
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
        # Reverse the question: with k eggs and m attempts, how many floors can we test?
        # Drop an egg; it may break or survive.
        # If it survives, we can handle dp[k][m-1] floors; if it breaks, dp[k-1][m-1] floors; add the floor of this drop.
        # Thus: dp[k][m] = dp[k][m-1] + dp[k-1][m-1] + 1.
        # The problem becomes finding the smallest m such that dp[k][m] >= n
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
