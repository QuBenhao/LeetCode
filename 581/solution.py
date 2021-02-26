import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findUnsortedSubarray(list(test_input))

    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m, end = float("-inf"), -1
        for i, n in enumerate(nums):
            if n > m:
                m = n
            elif n < m:
                end = i
        m,start = float("inf"), len(nums)
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < m:
                m = nums[i]
            elif nums[i] > m:
                start = i
        if start == len(nums) or end == -1:
            return 0
        return end - start + 1
