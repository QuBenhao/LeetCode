import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxProductDifference(list(test_input))

    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]
