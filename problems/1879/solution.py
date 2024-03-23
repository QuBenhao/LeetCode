import solution
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumXORSum(*test_input)

    def minimumXORSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        @lru_cache(None)
        def dfs(idx, vals):
            if idx == len(nums1) - 1:
                return nums1[idx] ^ vals[0]
            ans = float("inf")
            for val in vals:
                tp = list(vals)
                tp.remove(val)
                ans = min(ans, dfs(idx+1,tuple(tp)) + (nums1[idx] ^ val))
            return ans
        return dfs(0, tuple(sorted(nums2)))
