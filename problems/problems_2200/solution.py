import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findKDistantIndices(*test_input)

    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        last, n = 0, len(nums)
        for i, num in enumerate(nums):
            if num != key:
                continue
            last = max(last, i - k)
            for j in range(last, min(n, i + k + 1)):
                ans.append(j)
            last = i + k + 1
        return ans
