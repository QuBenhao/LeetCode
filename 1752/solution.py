import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.check(list(test_input))

    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(len(nums)):
            if nums[i-1] > nums[i]:
                count += 1
        return count <= 1
