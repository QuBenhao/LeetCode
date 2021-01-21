import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, k = test_input
        return self.mostCompetitive(list(nums), k)

    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        window = []
        for i in range(len(nums)):
            while window and window[-1] > nums[i] and len(window) + len(nums) - i > k:
                window.pop()
            if len(window) < k:
                window.append(nums[i])
        return window
