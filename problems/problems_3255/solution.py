import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.resultsArray(*test_input)

    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * (n - k + 1)
        cnt = 0
        for i, num in enumerate(nums):
            cnt = cnt + 1 if i == 0 or num == nums[i - 1] + 1 else 1
            if cnt >= k:
                ans[i - k + 1] = num
        return ans
