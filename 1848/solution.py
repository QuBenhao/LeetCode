import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, target, start = test_input
        return self.getMinDistance(list(nums), target, start)

    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        ans = float("inf")
        for i, num in enumerate(nums):
            if num == target:
                ans = min(ans, abs(start - i))
        return ans
