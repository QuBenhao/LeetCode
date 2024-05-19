import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.rob(list(test_input))

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans1 = ans2 = 0
        for num in nums:
            ans1, ans2 = ans2 + num, max(ans1, ans2)
        return max(ans1, ans2)
