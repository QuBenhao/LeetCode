import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxFrequency(*test_input)

    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()

        n = len(nums)
        ans = cnt = left = right = left2 = 0
        for i, x in enumerate(nums):
            while nums[left2] < x - k * 2:
                left2 += 1
            ans = max(ans, min(i - left2 + 1, numOperations))

            cnt += 1
            # 循环直到连续相同段的末尾，这样可以统计出 x 的出现次数
            if i < n - 1 and x == nums[i + 1]:
                continue
            while nums[left] < x - k:
                left += 1
            while right < n and nums[right] <= x + k:
                right += 1
            ans = max(ans, min(right - left, cnt + numOperations))
            cnt = 0

        return ans
