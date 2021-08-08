import solution
from functools import lru_cache
from math import inf


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, k = test_input
        return self.minSpaceWastedKResizing(list(nums), k)

    def minSpaceWastedKResizing(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)

        @lru_cache(None)
        def dfs(idx, left):
            if idx == n:
                return 0
            if not left:
                m = max(nums[idx:])
                return m * (n - idx)
            m = 0
            ans = inf
            for i in range(idx, n):
                m = max(m, nums[i])
                ans = min(ans, dfs(i+1, left - 1) + m * (i+1 - idx))
            return ans
        return dfs(0, k) - sum(nums)
