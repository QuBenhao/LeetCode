import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        length = self.removeDuplicates(test_input)
        return length, test_input[:length]

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack_size = 2  # Stack size; keep the first two elements by default
        for i in range(2, len(nums)):
            if nums[i] != nums[stack_size - 2]:  # Compare with the element below the top of the stack
                nums[stack_size] = nums[i]  # Push onto the stack
                stack_size += 1
        return min(stack_size, len(nums))
