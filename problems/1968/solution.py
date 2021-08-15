import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.rearrangeArray(list(test_input))

    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = (len(nums) + 1) // 2
        nums[::2], nums[1::2] = nums[:n], nums[n:]
        return nums
