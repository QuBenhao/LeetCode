import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.divideArray(*test_input)

    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(0, n, 3):
            if nums[i + 2] - nums[i] <= k:
                ans.append(nums[i:i + 3])
            else:
                return []
        return ans
