import solution
import bisect
from math import inf


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums1, nums2 = test_input
        return self.minAbsoluteSumDiff(list(nums1), list(nums2))

    def minAbsoluteSumDiff(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        diff = sum(abs(nums1[i] - nums2[i]) for i in range(n))
        if not diff:
            return 0
        ans = inf
        sl = sorted(nums1)
        for i, num in enumerate(nums2):
            idx = bisect.bisect_left(sl, num)
            # idx > 0 尝试用idx-1替换当前值
            if idx:
                ans = min(ans, diff - abs(nums1[i] - nums2[i]) + abs(sl[idx - 1] - nums2[i]))
            # idx < n 尝试用idx替换当前值
            if idx < n:
                ans = min(ans, diff - abs(nums1[i] - nums2[i]) + abs(sl[idx] - nums2[i]))
        return ans % (10 ** 9 + 7)
