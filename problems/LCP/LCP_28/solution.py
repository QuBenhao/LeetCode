import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, target = test_input
        return self.purchasePlans(list(nums), target)

    def purchasePlans(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        nums.sort()
        left, right = 0, len(nums) - 1
        ans = 0
        while left < right:
            # The current left and right pointers do not form a valid pair; the sum must decrease
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                ans += right - left
                left += 1
        return ans % mod
