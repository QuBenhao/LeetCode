import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        inputs = list(inputs)
        nums = inputs[0].pop()
        obj = NumArray(nums)
        ans = [None]
        for i in range(1, len(ops)):
            ans.append(obj.sumRange(inputs[i][0],inputs[i][1]))
        return ans


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.sum[i+1] = nums[i] + self.sum[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum[j+1] - self.sum[i]
