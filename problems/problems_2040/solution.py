from bisect import bisect_left

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.kthSmallestProduct(*test_input)

    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        zero1 = bisect_left(nums1, 0)
        zero2 = bisect_left(nums2, 0)
        m, n = len(nums1), len(nums2)

        def check(x):
            if x < 0:
                cnt = 0

                # 右上
                i, j = 0, zero2
                while i < zero1 and j < n:
                    if nums1[i] * nums2[j] > x:
                        j += 1
                    else:
                        cnt += n - j
                        i += 1
                # 左下
                i, j = zero1, 0
                while i < m and j < zero2:
                    if nums1[i] * nums2[j] > x:
                        i += 1
                    else:
                        cnt += m - i
                        j += 1
            else:
                cnt = zero1 * (n - zero2) + (m - zero1) * zero2

                # 左上
                i, j = 0, zero2 - 1
                while i < zero1 and j >= 0:
                    if nums1[i] * nums2[j] > x:
                        i += 1
                    else:
                        cnt += zero1 - i
                        j -= 1
                # 右下
                i, j = zero1, n - 1
                while i < m and j >= zero2:
                    if nums1[i] * nums2[j] > x:
                        j -= 1
                    else:
                        cnt += j - zero2 + 1
                        i += 1
            return cnt >= k

        corners = (nums1[0] * nums2[0],
                   nums1[0] * nums2[-1],
                   nums1[-1] * nums2[0],
                   nums1[-1] * nums2[-1])
        left, right = min(corners), max(corners)
        return left + bisect_left(range(left, right), True, key=check)
