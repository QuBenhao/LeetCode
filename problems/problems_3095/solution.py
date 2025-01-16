from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumSubarrayLength(*test_input)

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = inf
        for i, x in enumerate(nums):
            if x >= k:
                return 1
            j = i - 1
            while j >= 0 and nums[j] | x != nums[j]:
                nums[j] |= x
                if nums[j] >= k:
                    ans = min(ans, i - j + 1)
                j -= 1
        return ans if ans < inf else -1
