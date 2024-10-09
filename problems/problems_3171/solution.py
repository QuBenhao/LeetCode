import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumDifference(*test_input)

    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = abs(nums[0] - k)
        for i, num in enumerate(nums):
            ans = min(ans, abs(num - k))
            j = i - 1
            while j >= 0 and nums[j] | num != nums[j]:
                nums[j] |= num
                ans = min(ans, abs(nums[j] - k))
                j -= 1
        return ans
