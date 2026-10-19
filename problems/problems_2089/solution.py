from bisect import bisect_left, bisect_right

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.targetIndices(*test_input)

    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        return [i for i in range(bisect_left(nums, target), bisect_right(nums, target))]
