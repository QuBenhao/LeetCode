import solution
from typing import *
from math import inf


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumSum(test_input)

    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        left_min, right_min = [inf] * n, [inf] * n
        for i in range(n):
            left_min[i] = min(left_min[i - 1], nums[i])
            right_min[n - 1 - i] = min(right_min[min(n - i, n - 1)], nums[n - 1 - i])
        ans = inf
        for i in range(1, n - 1):
            if nums[i] > left_min[i - 1] and nums[i] > right_min[i + 1]:
                ans = min(ans, left_min[i - 1] + right_min[i + 1] + nums[i])
        return ans if ans != inf else -1
