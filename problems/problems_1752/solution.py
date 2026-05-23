from itertools import pairwise

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.check(list(test_input))

    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        decr = nums[-1] > nums[0]
        for a, b in pairwise(nums):
            if a > b:
                if decr:
                    return False
                decr = True
        return True
