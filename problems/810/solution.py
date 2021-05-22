import solution
from functools import reduce
from operator import xor


class Solution(solution.Solution):
    def solve(self, test_input):
        return self.xorGame(list(test_input))

    def xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) % 2 == 0 or reduce(xor, nums) == 0
