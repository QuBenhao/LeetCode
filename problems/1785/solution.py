import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, limit, goal = test_input
        return self.minElements(list(nums), limit, goal)

    def minElements(self, nums, limit, goal):
        """
        :type nums: List[int]
        :type limit: int
        :type goal: int
        :rtype: int
        """
        import math
        return int(math.ceil(float(abs(sum(nums) - goal)) / limit))
