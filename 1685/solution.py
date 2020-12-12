import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getSumAbsoluteDifferences(test_input)

    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        results = [0] * len(nums)
        results[0] = sum(nums[1:]) - (len(nums) -1) * nums[0]
        for i in range(1,len(nums)):
            results[i] = results[i-1] + (2*i-len(nums)) * (nums[i] - nums[i-1])
        return results
