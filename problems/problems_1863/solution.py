from functools import reduce
from operator import or_

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.subsetXORSum(list(test_input))

    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Each number appears 2^(n-1) times
        return reduce(or_, nums) << (len(nums) - 1)
