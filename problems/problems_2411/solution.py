from typing import *

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.smallestSubarrays(test_input)

    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        # LogTrick
        ans = [1] * len(nums) # The subarray length is at least 1
        for i, x in enumerate(nums): # Compute the OR of subarrays ending at i
            for j in range(i - 1, -1, -1):
                if (nums[j] | x) == nums[j]: # nums[j] and the elements to its left cannot increase
                    break
                nums[j] |= x # nums[j] increases; it now equals the OR of the original elements from nums[j] through nums[i]
                ans[j] = i - j + 1 # The subarray length when nums[j] last increases is the answer
        return ans
