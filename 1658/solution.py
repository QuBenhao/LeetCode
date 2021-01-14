import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, x = test_input
        return self.minOperations(list(nums), x)

    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        target = sum(nums) - x
        n = len(nums)

        if target < 0:
            return -1
        if target == 0:
            return n

        curr_sum = 0
        left = 0
        max_length = 0
        for i,num in enumerate(nums):
            curr_sum += num
            while curr_sum > target:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == target:
                max_length = max(max_length, i - left + 1)
        if not max_length:
            return -1
        return n - max_length
