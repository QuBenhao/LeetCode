import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.hasIncreasingSubarrays(*test_input)

    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        a, b = 0, k
        n = len(nums) - k
        while b <= n:
            for j in range(a + 1, b):
                if nums[j] <= nums[j - 1]:
                    b += j - a
                    a += j - a
                    break
            else:
                for j in range(b + 1, b + k):
                    if nums[j] <= nums[j - 1]:
                        a += j - b
                        b += j - b
                        break
                else:
                    return True
        return False
