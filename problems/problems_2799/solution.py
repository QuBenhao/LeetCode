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
            # 以left为左边界，right到n为右边界的子数组均满足条件
            if len(window) == len(uniques):
                ans += n - right + 1
            window[num] -= 1
            if window[num] == 0:
                del window[num]
        return ans
