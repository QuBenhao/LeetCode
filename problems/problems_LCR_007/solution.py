import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.threeSum(test_input)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                while i + 1 < left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right < n - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                if left >= right:
                    break
                if nums[left] + nums[right] == -nums[i]:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                else:
                    right -= 1
        return ans
