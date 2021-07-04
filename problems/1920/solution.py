import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.buildArray(list(test_input))

    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [nums[nums[i]] for i in range(len(nums))]
