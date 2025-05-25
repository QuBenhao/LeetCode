import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.peakIndexInMountainArray(test_input)

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
