import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.pivotArray(*test_input)

    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, equal, greater = [], [], []
        for x in nums:
            if x < pivot:
                less.append(x)
            elif x > pivot:
                greater.append(x)
            else:
                equal.append(x)
        return less + equal + greater

