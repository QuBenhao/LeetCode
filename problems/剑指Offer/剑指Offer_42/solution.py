import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxSubArray(list(test_input))

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, cur = nums[0], 0
        for num in nums:
            cur = max(cur + num, num)
            ans = max(cur, ans)
        return ans
