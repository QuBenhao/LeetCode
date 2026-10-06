from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countCompleteSubarrays(test_input)

    def countCompleteSubarrays(self, nums: List[int]) -> int:
        uniques = set(nums)
        window = defaultdict(int)
        ans = right = 0
        n = len(nums)
        for num in nums:
            while right < n and len(window) < len(uniques):
                window[nums[right]] += 1
                right += 1
            # Subarrays with left boundary left and right boundary from right through n all satisfy the condition
            if len(window) == len(uniques):
                ans += n - right + 1
            window[num] -= 1
            if window[num] == 0:
                del window[num]
        return ans
