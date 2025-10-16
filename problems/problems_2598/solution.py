import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findSmallestInteger(*test_input)

    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        counts = [0] * value
        for num in nums:
            counts[num % value] += 1
        m = min(counts)
        return m * value + counts.index(m)
