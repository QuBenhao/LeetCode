import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.containsNearbyDuplicate(*test_input)

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for i, num in enumerate(nums):
            if num in window:
                return True
            window.add(num)
            if i >= k:
                window.remove(nums[i - k])
        return False
