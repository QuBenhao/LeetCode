import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.permute(test_input)

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(x):
            if x == len(nums) - 1:
                ans.append(list(nums))
                return
            for i in range(x, len(nums)):
                nums[i], nums[x] = nums[x], nums[i]
                dfs(x + 1)
                nums[i], nums[x] = nums[x], nums[i]

        dfs(0)
        return ans
