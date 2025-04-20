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
        # 每个数出现的次数是 2^(n-1) 次
        return reduce(or_, nums) << (len(nums) - 1)
