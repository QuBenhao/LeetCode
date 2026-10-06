from itertools import accumulate, pairwise
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxSumTrionic(test_input)

    def maxSumTrionic(self, nums: List[int]) -> int:
        ans = dp1 = dp2 = dp3 = -inf
        for a, b in pairwise(nums):
            dp3 = max(dp3, dp2) + b if a < b else -inf
            dp2 = max(dp2, dp1) + b if a > b else -inf
            dp1 = max(dp1, a) + b if a < b else -inf
            ans = max(ans, dp3)
        return ans

    #     n = len(nums)
    #     # split arr by equals adjacent
    #     last = idx = 0
    #     splits = []
    #     while idx < n - 1:
    #         if nums[idx] == nums[idx + 1]:
    #             splits.append(nums[last:idx+1])
    #             last = idx + 1
    #         idx += 1
    #     if last == 0:
    #         return self.process_each(nums)
    #     splits.append(nums[last:])
    #     return max(self.process_each(s) for s in splits)
    #
    # def process_each(self, nums: List[int]) -> int:
    #         if not nums:
    #             return -inf
    #
    #         pre_sum = [0] + list(accumulate(nums))
    #         n = len(nums)
    #         ans = -inf
    #         idx = 0
    #         lz = -1
    #         while idx < n - 1:
    #             if lz != -1:
    #                 # The increasing segment has already been traversed
    #                 l = idx
    #             else:
    #                 l = idx
    #                 while l < n - 1 and nums[l] < nums[l + 1]:
    #                     if lz == -1 and nums[l] >= 0:
    #                         lz = l
    #                     l += 1
    #                 # No first increasing segment was found
    #                 if l == idx or l == n - 1:
    #                     idx += 1
    #                     lz = -1
    #                     continue
    #                 # Include as few negative numbers as possible
    #                 if lz == -1:
    #                     lz = l - 1
    #             q = l
    #             while q < n - 1 and nums[q] > nums[q + 1]:
    #                 q += 1
    #             # No valid segment remains
    #             if q == n - 1:
    #                 break
    #             # Find the end of the third, increasing segment
    #             r = q
    #             tmp = lz
    #             # Reduce repeated counting of increasing segments
    #             lz = -1
    #             while r < n - 1 and nums[r] < nums[r + 1]:
    #                 if lz == -1 and nums[r] >= 0:
    #                     lz = r
    #                 r += 1
    #             if lz == -1:
    #                 lz = r - 1
    #             # q + 2: the last segment may be entirely negative, so include as few elements as possible
    #             ans = max(ans, pre_sum[r + 1] - pre_sum[tmp], pre_sum[q + 2] - pre_sum[tmp])
    #             idx = r
    #         return ans
