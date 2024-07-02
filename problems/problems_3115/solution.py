import solution
from typing import *
from math import isqrt


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumPrimeDifference(test_input)

    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def is_prime(n: int) -> bool:
            return n >= 2 and all(n % i for i in range(2, isqrt(n) + 1))

        left, right = 0, len(nums) - 1
        while left < right:
            if is_prime(nums[left]):
                break
            left += 1
        while left < right:
            if is_prime(nums[right]):
                break
            right -= 1
        return right - left
