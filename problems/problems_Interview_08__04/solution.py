import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.subsets(test_input)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def dfs(idx, path):
            if idx == n:
                ans.append(list(path))
                return
            dfs(idx + 1, path)
            path.append(nums[idx])
            dfs(idx + 1, path)
            path.pop()

        dfs(0, [])
        return ans
