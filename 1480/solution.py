import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.runningSum(nums=test_input)

    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum_arr = nums
        for i in range(len(nums)):
            if i > 0:
                sum_arr[i] = sum_arr[i - 1] + nums[i]
        return sum_arr
