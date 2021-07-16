import solution
import bisect


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, target = test_input
        return self.search(list(nums), target)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return bisect.bisect_right(nums, target) - bisect.bisect_left(nums, target)
