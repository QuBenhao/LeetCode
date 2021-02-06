import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxAbsoluteSum(list(test_input))

    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_sum = [0] * n
        min_sum = [0] * n
        ans = abs(nums[0])
        max_sum[0] = nums[0]
        min_sum[0] = nums[0]
        for i in range(1,n):
            max_sum[i] = max(max_sum[i-1] + nums[i], nums[i])
            min_sum[i] = min(min_sum[i-1] + nums[i], nums[i])
            ans = max(abs(max_sum[i]), abs(min_sum[i]), ans)
        return ans
