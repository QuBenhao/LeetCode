import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumAddedInteger(*test_input)

    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        for i in range(2, -1, -1):
            quota, diff, idx, valid = 2 - i, nums2[0] - nums1[i], i + 1, True
            for i in range(1, len(nums2)):
                while nums2[i] - nums1[idx] != diff:
                    if not quota:
                        valid = False
                        break
                    quota -= 1
                    idx += 1
                if not valid:
                    break
                idx += 1
            if valid:
                return diff
        return nums2[0] - nums1[0]
