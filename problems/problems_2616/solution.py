import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimizeMax(*test_input)

    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def check(max_diff: int) -> bool:
            count = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= max_diff:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= p

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
