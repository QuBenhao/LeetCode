import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.subsets(test_input)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(idx: int, path: List[int]):
            if idx == len(nums):
                ans.append(list(path))
                return
            # Skip the current number
            backtrack(idx + 1, path)
            # Select the current number
            path.append(nums[idx])
            backtrack(idx + 1, path)
            # backtrack
            path.pop()

        backtrack(0, [])
        return ans
