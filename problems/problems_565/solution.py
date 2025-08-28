import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.arrayNesting(test_input)

    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        visited = [False] * n
        for i in range(n):
            if visited[i]:
                continue
            cur = 1
            visited[i] = True
            j = nums[i]
            while j != i:
                visited[j] = True
                cur += 1
                j = nums[j]
            ans = max(ans, cur)
        return ans
