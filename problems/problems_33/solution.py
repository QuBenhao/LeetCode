import solution
from typing import *
from bisect import bisect_left


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.search(*test_input)

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        idx = bisect_left(nums, True, key=lambda x: x < nums[0])
        ans = bisect_left(range(idx, n + idx - 1), True, key=lambda x: nums[x % n] >= target)
        return (idx + ans) % n if nums[(idx + ans) % n] == target else -1

        # n = len(nums)
        # idx = bisect_left(nums, True, key=lambda x: x < nums[0])
        # left, right = idx, n + idx - 1
        # while left < right:
        #     mid = (left + right) // 2
        #     if nums[mid % n] < target:
        #         left = mid + 1
        #     else:
        #         right = mid
        # return left % n if nums[left % n] == target else -1

        # if target == nums[0]:
        #     return 0
        # left, right = 0, len(nums)
        # while left < right:
        #     mid = (left + right) // 2
        #     if nums[mid] < nums[0]:
        #         right = mid
        #     else:
        #         left = mid + 1
        #
        # idx = left
        # if target > nums[0]:
        #     left, right = 0, idx
        # else:
        #     left, right = idx, len(nums)
        # while left < right:
        #     mid = (left + right) // 2
        #     if nums[mid] < target:
        #         left = mid + 1
        #     else:
        #         right = mid
        # return left if 0 <= left < len(nums) and nums[left] == target else -1
