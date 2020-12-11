import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.removeDuplicates(test_input)

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]

        return index + 1,nums[:index+1]