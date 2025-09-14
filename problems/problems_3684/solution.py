import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxKDistinct(*test_input)

    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        return list(sorted(set(nums), reverse=True))[:k]
