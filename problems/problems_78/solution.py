import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.subsets(test_input)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(arr: List[int], idx: int):
            if idx == len(nums):
                ans.append(list(arr))
                return
            dfs(arr, idx + 1)
            arr.append(nums[idx])
            dfs(arr, idx + 1)
            arr.pop()

        ans = []
        dfs([], 0)
        return ans
