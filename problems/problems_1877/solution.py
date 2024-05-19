import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minPairSum(list(test_input))

    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 0
        left, right = 0, len(nums) - 1
        while left < right:
            ans = max(ans, nums[left] + nums[right])
            left += 1
            right -=1
        return ans
