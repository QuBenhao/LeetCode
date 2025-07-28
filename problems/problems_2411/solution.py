from typing import *

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.smallestSubarrays(test_input)

    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        # LogTrick
        ans = [1] * len(nums) # 子数组的长度至少是 1
        for i, x in enumerate(nums): # 计算右端点为 i 的子数组的或值
            for j in range(i - 1, -1, -1):
                if (nums[j] | x) == nums[j]: # nums[j] 及其左边元素无法增大
                    break
                nums[j] |= x # nums[j] 增大，现在 nums[j] = 原数组 nums[j] 到 nums[i] 的或值
                ans[j] = i - j + 1 # nums[j] 最后一次增大时的子数组长度就是答案
        return ans
