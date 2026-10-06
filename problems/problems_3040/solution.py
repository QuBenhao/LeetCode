import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxOperations(test_input)

    def maxOperations(self, nums: List[int]) -> int:
        @cache  # Cache decorator to avoid recomputing dfs results (memoization)
        def dfs(i: int, j: int, target: int) -> int:
            nonlocal done
            if done:
                return 0
            if i >= j:
                done = True
                return 0
            res = 0
            if nums[i] + nums[i + 1] == target:  # Remove the first two numbers
                res = max(res, dfs(i + 2, j, target) + 1)
            if nums[j - 1] + nums[j] == target:  # Remove the last two numbers
                res = max(res, dfs(i, j - 2, target) + 1)
            if nums[i] + nums[j] == target:  # Remove the first and last numbers
                res = max(res, dfs(i + 1, j - 1, target) + 1)
            return res

        done = False
        n = len(nums)
        res1 = dfs(2, n - 1, nums[0] + nums[1])  # Remove the first two numbers
        res2 = dfs(0, n - 3, nums[-2] + nums[-1])  # Remove the last two numbers
        res3 = dfs(1, n - 2, nums[0] + nums[-1])  # Remove the first and last numbers
        return max(res1, res2, res3) + 1  # Include the first operation

