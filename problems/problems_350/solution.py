import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.intersect(*test_input)

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # # Approach 1: Sort, then compare with two pointers
        # nums1.sort()
        # nums2.sort()
        # ans = []
        # idx1 = idx2 = 0
        # n1, n2 = len(nums1), len(nums2)
        # while idx1 < n1 and idx2 < n2:
        #     if nums1[idx1] == nums2[idx2]:
        #         ans.append(nums1[idx1])
        #         idx1 += 1
        #         idx2 += 1
        #     elif nums1[idx1] > nums2[idx2]:
        #         idx2 += 1
        #     else:
        #         idx1 += 1
        # return ans
    
        # Approach 2: Compare frequency counts
        c1, c2 = Counter(nums1), Counter(nums2)
        ans = []
        for k in c1 & c2:
            ans.extend([k] * min(c1[k], c2[k]))
        return ans
