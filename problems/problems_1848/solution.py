import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getMinDistance(*test_input)

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
