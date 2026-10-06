import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxDistance(test_input)

    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        # If the endpoint colors differ, return the maximum distance directly
        if colors[0] != colors[-1]:
            return n - 1

        # Scan from right to left for the first position whose color differs from the first
        right = n - 1
        while right > 0 and colors[right] == colors[0]:
            right -= 1

        # Scan from left to right for the first position whose color differs from the last
        left = 0
        while left < n - 1 and colors[left] == colors[-1]:
            left += 1

        return max(right, n - 1 - left)
