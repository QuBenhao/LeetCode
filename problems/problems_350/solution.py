import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.intersect(*test_input)

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # # 解法一： 排序后双指针对比
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
    
        # 解法二： 哈希计数对比
        c1, c2 = Counter(nums1), Counter(nums2)
        ans = []
        for k in c1 & c2:
            ans.extend([k] * min(c1[k], c2[k]))
        return ans
