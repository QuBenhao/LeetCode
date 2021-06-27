import solution
from math import inf


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canBeIncreasing(list(test_input))

    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        idx = None
        for i in range(len(nums) - 1):
            if nums[i + 1] <= nums[i]:
                idx = i
                break
        if idx is None:
            return True
        nums1 = nums[:idx] + nums[idx + 1:]
        nums2 = nums[:idx + 1] + nums[idx + 2:]
        ans1 = ans2 = True
        for i in range(len(nums1) - 1):
            if nums1[i + 1] <= nums1[i]:
                ans1 = False
            if nums2[i + 1] <= nums2[i]:
                ans2 = False
        return ans1 or ans2
