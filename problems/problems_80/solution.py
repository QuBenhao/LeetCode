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
        stack_size = 2  # 栈的大小，前两个元素默认保留
        for i in range(2, len(nums)):
            if nums[i] != nums[stack_size - 2]:  # 和栈顶下方的元素比较
                nums[stack_size] = nums[i]  # 入栈
                stack_size += 1
        return min(stack_size, len(nums))
